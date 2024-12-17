# Event Management App

## Overview

This is a Django-based web application for managing events. The application allows users to register, log in, create events, and attend events. It showcases core features of Django, including authentication, forms, models, and views, and includes a REST API for managing event data.

---

## Setting Up the Project

### 1. Create a Virtual Environment

To isolate the project dependencies, create a virtual environment:

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

Once the virtual environment is activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Database Migrations

### 1. Create Migrations

Generate migration files for the database schema based on your models:

```bash
python manage.py makemigrations
```

### 2. Apply Migrations

Apply the generated migrations to set up the database:

```bash
python manage.py migrate
```

---

## Starting the Development Server

Run the following command to start the Django development server:

```bash
python manage.py runserver
```

The application will be accessible at: `http://127.0.0.1:8000/`

---

## Concepts Covered

This project demonstrates the following core Django concepts:

1. **User Authentication:**

   - Register and log in using Django's built-in authentication system.

2. **Forms:**

   - Custom user registration form with Django's `UserCreationForm`.
   - Event Create/Update form to handle event data.
   - Event deletion functionality using Django's views.

3. **Models and ORM:**

   - Event model with relationships (e.g., `ForeignKey`, `ManyToManyField`).

4. **Views:**

   - Function-based views (FBVs) and class-based views (CBVs).

5. **Templates:**

   - Dynamic HTML with Django Template Language (DTL).

6. **REST API (Optional):**

   - Endpoints for event CRUD operations using Django REST Framework.

---

## Extend the Project

To encourage further learning, consider adding the following features:

1. **Event Search and Filtering:**
   - Add functionality to search and filter events based on criteria like date, location, or title.

2. **User Profiles:**
   - Enable users to update their profiles and view other users' event participation.

3. **Event Reviews:**
   - Allow attendees to leave reviews or feedback on events.

4. **Pagination:**
   - Implement pagination for event listings to improve usability.

5. **API Authentication:**
   - Secure API endpoints with token-based authentication using Django REST Framework.

Enjoy building and managing your events!

