from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    """
    RegisterUserForm is a form for registering a new user.
    This form extends the UserCreationForm and includes additional fields for email, first name, and last name.
    Attributes:
        email (EmailField): A field for the user's email address.
        first_name (CharField): A field for the user's first name with a maximum length of 50 characters.
        last_name (CharField): A field for the user's last name with a maximum length of 50 characters.
    Meta:
        model (User): The model associated with this form.
        fields (list): A list of fields to be included in the form, which are 'username', 'first_name', 'last_name', 'email', 'password1', and 'password2'.
    """

    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
