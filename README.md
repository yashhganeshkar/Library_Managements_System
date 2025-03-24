# Library Management System

## Overview

This project is a **Library Management System** built using **Django** and **Django REST Framework (DRF)**, with **MySQL** as the database. It allows **admins** to manage books and provides a **student view** to list all books.

## Features

### Admin Operations:

- **Signup:** Create a new admin account (email must be unique).
- **Login:** Authenticate admins using email and password.
- **Book Management:**
  - Create: Add new books.
  - Read: Retrieve all books.
  - Update: Edit book details.
  - Delete: Remove a book.

### Student View:

- View all available books in the library.

## Technologies Used

- **Backend:** Django, Django REST Framework
- **Database:** MySQL
- **Authentication:** Django built-in authentication
- **Frontend (Optional):** Django Templates (for student book listing)

## Installation & Setup

### Prerequisites

Ensure you have the following installed:

- Python (>=3.8)
- MySQL Server
- pip (Python package manager)
- Virtual Environment (recommended)

### Steps to Setup the Project

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/library-management.git
cd library-management
```

#### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Configure MySQL Database

Update the `settings.py` file with your MySQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

#### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 6. Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Enter your admin email and password when prompted.

#### 7. Start the Development Server

```bash
python manage.py runserver
```

Access the application at: `http://127.0.0.1:8000/`

## API Endpoints

### **Authentication**

- **Register Admin:** `POST /register/`
- **Login Admin:** `POST /admin/login/`

### **Book Management (Admin Only)**

- **Create Book:** `POST /create/`
- **Update Book:** `POST /<book_id>/edit/`
- **Delete Book:** `POST /<book_id>/delete/`

### **Student View**

- **View Books:** `GET /`
- **Book Details:** `GET /details/<book_id>`

## Usage

### Register an Admin

```json
{
    "email": "admin@example.com",
    "username": "adminuser",
    "password": "securepassword"
}
```

### Login as Admin

```json
{
    "email": "admin@example.com",
    "password": "securepassword"
}
```

### Create a Book

```json
{
    "title": "Django for Beginners",
    "author": "William S. Vincent",
    "isbn": "978-1735467207",
    "publish_date": "2021-01-01"
}
```

## Contributing

Feel free to fork this repository and contribute! Submit a pull request for review.


