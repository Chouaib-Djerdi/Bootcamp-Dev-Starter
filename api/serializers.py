# Import the serializers module from Django REST framework
from rest_framework import serializers

# Import the Event model from the events app
from events.models import Event


# Define a serializer class for the Event model
class EventSerializer(serializers.ModelSerializer):
    # Meta class to specify the model and fields to include in the serializer
    class Meta:
        # Specify the model to use for the serializer
        model = Event
        # Include all fields from the Event model in the serializer
        fields = "__all__"
