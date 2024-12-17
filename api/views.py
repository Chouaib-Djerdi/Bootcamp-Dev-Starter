from django.shortcuts import render
from rest_framework.decorators import api_view
from events.models import Event 
from .serializers import EventSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Function-based view to handle GET and POST requests for the event list
@api_view(['GET', 'POST'])
def event_list(request):
    if request.method == 'GET':
        # Handle GET request: retrieve all events and serialize them
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # Handle POST request: deserialize the request data and save a new event
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# Class-based view to handle GET and DELETE requests for a single event
class EventDetail(APIView):
    def get(self, request, pk):
        # Handle GET request: retrieve a single event by its primary key (id)
        try:
            event = Event.objects.get(id=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def delete(self, request, pk):
        # Handle DELETE request: delete a single event by its primary key (id)
        try:
            event = Event.objects.get(id=pk)
            event.delete()
            return Response(status=204)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)