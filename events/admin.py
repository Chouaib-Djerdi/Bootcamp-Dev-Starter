from django.contrib import admin

"""
This module registers the Event model with the Django admin site.
Imports:
    from django.contrib import admin: Imports the Django admin module.
    from .models import Event: Imports the Event model from the current package.
Functionality:
    admin.site.register(Event): Registers the Event model with the Django admin site, 
    allowing it to be managed through the admin interface.
"""
from .models import Event

# Register your models here.

admin.site.register(Event)
