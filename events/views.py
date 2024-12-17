from django.shortcuts import render, redirect
from .models import Event
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from django.urls import reverse

# The @login_required decorator ensures that only authenticated users can access these views.


@login_required
def event_listing(request):
    # Retrieve all Event objects from the database.
    events = Event.objects.all()
    # Render the 'event_listing.html' template with the events data.
    return render(request, "events/event_listing.html", {"events": events})


@login_required
def event_detail(request, event_id):
    # Retrieve a single Event object by its ID.
    event = Event.objects.get(id=event_id)
    # Render the 'event_detail.html' template with the event data.
    return render(request, "events/event_detail.html", {"event": event})


@login_required
def add_event(request):
    if request.method == "POST":
        # If the request method is POST, create a form instance with the submitted data.
        form = EventForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the event but don't commit to the database yet.
            event = form.save(commit=False)
            # Set the organizer of the event to the current user.
            event.organizer = request.user
            # Save the event to the database.
            event.save()
            # Redirect to the event listing page.
            return redirect(reverse("events:event-listing"))
    else:
        # If the request method is GET, create an empty form instance.
        form = EventForm()
    # Render the 'add_event.html' template with the form.
    return render(request, "events/add_event.html", {"form": form})


@login_required
def my_events(request):
    # Retrieve all Event objects where the organizer is the current user.
    events = Event.objects.filter(organizer=request.user)
    # Render the 'my_events.html' template with the events data.
    return render(request, "events/my_events.html", {"events": events})


@login_required
def update_event(request, pk):
    # Retrieve the Event object by its primary key (pk).
    event = Event.objects.get(pk=pk)
    # Create a form instance with the submitted data or the existing event instance.
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        # If the form is valid, save the updated event to the database.
        form.save()
        # Redirect to the event listing page.
        return redirect(reverse("events:event-listing"))
    # Render the 'add_event.html' template with the form.
    return render(request, "events/add_event.html", {"form": form})


@login_required
def delete_event(request, pk):
    # Retrieve the Event object by its primary key (pk).
    event = Event.objects.get(id=pk)
    # Delete the event from the database.
    event.delete()
    # Redirect to the event listing page.
    return redirect(reverse("events:event-listing"))


@login_required
def attend_event(request, event_id):
    # Retrieve the Event object by its ID.
    event = Event.objects.get(id=event_id)
    # Add the current user to the event's attendees.
    event.attendees.add(request.user)
    # Redirect to the event detail page.
    return redirect(reverse("events:event-detail", args=[event_id]))


@login_required
def unattend_event(request, event_id):
    # Retrieve the Event object by its ID.
    event = Event.objects.get(id=event_id)
    # Remove the current user from the event's attendees.
    event.attendees.remove(request.user)
    # Redirect to the event detail page.
    return redirect(reverse("events:event-detail", args=[event_id]))


@login_required
def attended_events(request):
    # Retrieve all Event objects where the current user is an attendee.
    events = Event.objects.filter(attendees=request.user)
    # Render the 'attended_events.html' template with the events data.
    return render(request, "events/attended_events.html", {"events": events})
