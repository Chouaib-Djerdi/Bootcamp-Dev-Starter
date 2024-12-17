from django.shortcuts import (
    render,
    redirect,
)  # Import render and redirect functions from Django shortcuts
from .forms import (
    RegisterUserForm,
)  # Import the RegisterUserForm from the current package's forms module
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)  # Import authentication functions from Django's auth module
from django.urls import reverse  # Import reverse function to get URL by its name


# Create your views here.
def register_user(request):
    if request.method == "POST":  # Check if the request method is POST
        form = RegisterUserForm(
            request.POST
        )  # Create a form instance with the POST data
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the form data to create a new user
            username = form.cleaned_data[
                "username"
            ]  # Get the cleaned username from the form
            password = form.cleaned_data[
                "password1"
            ]  # Get the cleaned password from the form
            user = authenticate(
                request, username=username, password=password
            )  # Authenticate the user
            login(request, user)  # Log the user in

            return redirect(
                reverse("events:event-listing")
            )  # Redirect to the event listing page
    else:
        form = RegisterUserForm()  # Create a new blank form instance
    return render(
        request, "register.html", context={"form": form}
    )  # Render the registration page with the form


def login_user(request):
    if request.method == "POST":  # Check if the request method is POST
        username = request.POST["username"]  # Get the username from the POST data
        password = request.POST["password"]  # Get the password from the POST data
        user = authenticate(
            request, username=username, password=password
        )  # Authenticate the user
        if user is not None:  # Check if the user exists
            login(request, user)  # Log the user in
            return redirect(
                reverse("events:event-listing")
            )  # Redirect to the event listing page
        else:
            return redirect(
                "/users/login/"
            )  # Redirect to the login page if authentication fails

    else:
        return render(
            request, "login.html"
        )  # Render the login page if the request method is not POST


def logout_user(request):
    logout(request)  # Log the user out
    return redirect(reverse("users:login-user"))  # Redirect to the login page
