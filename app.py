from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)

app.secret_key = "secret_key"
app.permanent_session_lifetime = timedelta(minutes=15)

# DATABASE CONFIG
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'Root'
DB_NAME = 'virtual_classroom'


def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )


# HOME
@app.route('/')
def home():
    return render_template('home.html')

# DASHBOARD PAGE
@app.route('/dashboard')
def dashboard():

    if 'username' not in session:
        flash('Please login first!', 'warning')
        return redirect(url_for('login'))

    return render_template('dashboard.html')

# REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)

        conn = get_db_connection()
        cursor = conn.cursor()

        try:

            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, hashed_password)
            )

            conn.commit()

            flash('Registration successful!', 'success')

            return redirect(url_for('login'))

        except pymysql.MySQLError as e:

            if e.args[0] == 1062:
                flash('Email already exists!', 'danger')
            else:
                flash(f'Error: {str(e)}', 'danger')

        finally:
            cursor.close()
            conn.close()

    return render_template('register.html')


# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()

        try:

            cursor.execute(
                "SELECT * FROM users WHERE username=%s",
                (username,)
            )

            user = cursor.fetchone()

            if user and check_password_hash(user['password'], password):

                session.permanent = True
                session['username'] = username

                flash('Login successful!', 'success')

                return redirect(url_for('dashboard'))

            else:
                flash('Invalid credentials!', 'danger')

        finally:
            cursor.close()
            conn.close()

    return render_template('login.html')

# PROFILE PAGE
@app.route('/profile')
def profile():

    if 'username' not in session:
        flash('Please login first!', 'warning')
        return redirect(url_for('login'))

    return render_template('profile.html')


# # CONTENT PAGE
# @app.route('/content')
# def content():

#     if 'username' not in session:
#         flash('Please login first!', 'warning')
#         return redirect(url_for('login'))

#     courses = [
#         {
#             "title": "Python Programming",
#             "description": "Learn Python from beginner to advanced.",
#             "image": "./static/images/python.jpg",
#             "badge": "Beginner",
#             "link": "python"
#         },
#         {
#             "title": "Web Development",
#             "description": "Master HTML CSS JavaScript and Flask.",
#             "image": "./static/images/webdev.jpg",
#             "badge": "Popular",
#             "link": "web-dev"
#         },
#         {
#             "title": "AWS Cloud",
#             "description": "Learn AWS cloud deployment and services.",
#             "image": "./static/images/awscloude.jpg",
#             "badge": "Advanced",
#             "link": "aws"
#         }
#     ]

#     return render_template('dashboard.html', courses=courses)

# COURSES PAGE
@app.route('/courses')
def courses():

    if 'username' not in session:
        flash('Please login first!', 'warning')
        return redirect(url_for('login'))

    courses = [
        {
            "title": "Python Programming",
            "description": "Learn Python from beginner to advanced.",
            "image": "/static/images/python.jpg",
            "badge": "Beginner",
            "link": "python"
        },
        {
            "title": "Web Development",
            "description": "Master HTML CSS JavaScript and Flask.",
            "image": "/static/images/webdev.jpg",
            "badge": "Popular",
            "link": "web-dev"
        },
        {
            "title": "AWS Cloud",
            "description": "Learn AWS cloud deployment and services.",
            "image": "/static/images/awscloude.jpg",
            "badge": "Advanced",
            "link": "aws"
        }
    ]

    return render_template(
        'courses.html',
        courses=courses
    )
# ASSIGNMENTS PAGE
@app.route('/assignments')
def assignments():

    if 'username' not in session:
        flash('Please login first!', 'warning')
        return redirect(url_for('login'))

    assignments = [
        {
            "title": "Python Mini Project",
            "course": "Python Programming",
            "deadline": "10 June 2026"
        },
        {
            "title": "Portfolio Website",
            "course": "Web Development",
            "deadline": "15 June 2026"
        },
        {
            "title": "AWS Deployment Task",
            "course": "AWS Cloud",
            "deadline": "20 June 2026"
        }
    ]

    return render_template(
        'assignments.html',
        assignments=assignments
    )

# CERTIFICATES PAGE
@app.route('/certificates')
def certificates():

    if 'username' not in session:
        flash('Please login first!', 'warning')
        return redirect(url_for('login'))

    certificates = [
        {
            "title": "Python Programming",
            "date": "May 2026"
        },
        {
            "title": "Web Development",
            "date": "June 2026"
        }
    ]

    return render_template(
        'certificates.html',
        certificates=certificates
    )
# ENROLL
@app.route('/enroll/<course_name>')
def enroll(course_name):

    if 'username' not in session:
        flash('Please login first!', 'warning')
        return redirect(url_for('login'))

    flash(f'Successfully enrolled in {course_name}!', 'success')

    return redirect(url_for('dashboard'))


# LOGOUT
@app.route('/logout')
def logout():

    session.clear()

    flash('Logged out successfully!', 'info')

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)