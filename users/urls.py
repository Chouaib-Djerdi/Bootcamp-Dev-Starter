from django.urls import path

"""
URL configuration for the users app.
This module defines the URL patterns for user-related views such as registration, login, and logout.
Routes:
- /register/ : Handles user registration.
- /login/    : Handles user login.
- /logout/   : Handles user logout.
Each route is associated with a corresponding view function:
- register_user : View function to handle user registration.
- login_user    : View function to handle user login.
- logout_user   : View function to handle user logout.
The `app_name` is set to "users" to allow for namespacing of these URLs.
"""
from .views import register_user, login_user, logout_user

app_name = "users"

urlpatterns = [
    path("register/", register_user, name="register-user"),
    path("login/", login_user, name="login-user"),
    path("logout/", logout_user, name="logout-user"),
]
