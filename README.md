# Django Application(student management system)

This project is a web application built using the Django framework.
It demonstrates the core features of a Django-based backend, including routing, views, templates, and database interaction.

The project is structured to run locally and can be extended for real-world use.

---

## Features

* Django project and app structure
* URL routing
* Views and templates
* Models and database integration (SQLite by default)
* Static files handling
* Basic CRUD operations (if your app includes them)
* Organized code following standard Django practices

---

## Project Structure

```
project/
│
├── manage.py
├── requirements.txt
├── projectname/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
└── app/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── templates/
    └── ...
```

---

## Installation and Setup

### 1. Create a Virtual Environment

```
python -m venv venv
```

Activate it:

```
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Run Migrations

```
python manage.py migrate
```

---

### 4. Start the Development Server

```
python manage.py runserver
```

The application will be available at:

```
http://127.0.0.1:8000/
```

---

## How It Works

* The application receives requests through Django’s URL routing system.
* Views process data and return responses.
* Templates render the UI.
* Models interact with the database for storing and retrieving data.

This structure allows the project to grow and handle additional features as needed.

---

## Technologies Used

* Python
* Django
* HTML/CSS (templates)
* SQLite (default database)

