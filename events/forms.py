from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    """
    EventForm is a ModelForm for creating and updating Event instances.

    Attributes:
        Meta (class): A nested class that defines metadata for the EventForm.
            model (Event): The model that this form is associated with.
            fields (list): A list of fields to include in the form. The fields are:
                - 'title': The title of the event.
                - 'description': A brief description of the event.
                - 'date': The date when the event will take place.
                - 'location': The location where the event will be held.
                - 'max_seats': The maximum number of seats available for the event.
    """

    class Meta:
        model = Event
        fields = [
            "title",
            "description",
            "date",
            "location",
            "max_seats",
        ]
