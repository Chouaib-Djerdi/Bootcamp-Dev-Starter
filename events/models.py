from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):
    """
    Represents an event with details such as title, description, date, location,
    maximum number of seats, organizer, and attendees.
    Attributes:
        title (CharField): The title of the event.
        description (TextField): A detailed description of the event.
        date (DateTimeField): The date and time when the event is scheduled.
        location (CharField): The location where the event will take place.
        max_seats (IntegerField): The maximum number of seats available for the event.
        organizer (ForeignKey): A reference to the User who is organizing the event.
        attendees (ManyToManyField): A list of Users attending the event.
    Methods:
        __str__(): Returns a string representation of the event, which is its title.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    max_seats = models.IntegerField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(
        User, related_name="attending_events", blank=True
    )

    def __str__(self):
        return f"{self.title}"
