# 🎓 AWS Hosted Virtual Classroom And Learning Platform

A modern and responsive Learning Management System (LMS) built using Flask, MySQL, HTML, CSS, Bootstrap, and Chart.js.

This project provides an interactive virtual classroom experience where students can manage courses, assignments, certificates, and track learning progress through a professional dashboard.

---

## 🚀 Features

### 🔐 Authentication System

* User Registration
* Secure Login
* Logout Functionality
* Session Management
* Password Hashing

### 📊 Dashboard

* Learning Analytics
* Course Progress Tracking
* Recent Activity Section
* Notifications Panel
* Interactive Charts (Chart.js)

### 📚 Courses

* Browse Available Courses
* Course Cards
* Course Information
* Enrollment System

### 📝 Assignments

* Assignment Dashboard
* Deadlines Tracking
* Submission Section

### 🏆 Certificates

* View Certificates
* Download Certificate UI
* Achievement Tracking

### 👤 User Profile

* Profile Information
* Learning Statistics
* Activity History
* Modern Profile Interface

### 🎨 Modern UI

* Glassmorphism Design
* Responsive Layout
* Sidebar Navigation
* Gradient Effects
* Hover Animations
* Mobile Friendly

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Chart.js
* Font Awesome

### Backend

* Flask (Python)

### Database

* MySQL

### Authentication

* Werkzeug Security

---

## 📂 Project Structure

```bash
virtual-classroom/
│
├── app.py
│
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── courses.html
│   ├── assignments.html
│   ├── certificates.html
│   └── profile.html
│
├── static/
│   ├── style.css
│   └── images/
│
└── requirements.txt
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Rushijadhav1/aws-hosted-virtual-classroom.git
```

### Open Project

```bash
cd aws-hosted-virtual-classroom
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Project

```bash
python app.py
```

---

## 🗄️ Database Setup

Create MySQL Database:

```sql
CREATE DATABASE virtual_classroom;
```

Create Users Table:

```sql
CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    password TEXT
);
```

---

## 📸 Screenshots

### Dashboard

* Analytics Cards
* Progress Tracking
* Activity Feed

### Courses

* Modern Course Cards
* Enrollment System

### Assignments

* Assignment Tracking Interface

### Certificates

* Certificate Management Page

### Profile

* User Statistics
* Activity Overview

---

## 🌟 Future Improvements

* AWS S3 File Storage
* AWS EC2 Deployment
* AWS RDS Integration
* Video Lectures
* Assignment Upload System
* Admin Dashboard
* Real-Time Notifications
* Dark/Light Theme Toggle

---

## 👨‍💻 Author

**sourabh savale**

GitHub:
https://github.com/Sourabh-345

---

## 📄 License

This project is developed for educational and learning purposes.
