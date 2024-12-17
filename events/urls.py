from django.urls import path

"""
URL configuration for the events app.
This module defines the URL patterns for the events app, mapping URLs to their corresponding view functions.
Routes:
- "" : Displays the list of events.
- "<int:event_id>/" : Displays the details of a specific event.
- "add-event/" : Provides a form to add a new event.
- "my-events/" : Displays the events created by the logged-in user.
- "update-event/<int:pk>/" : Provides a form to update an existing event.
- "delete-event/<int:pk>/" : Deletes a specific event.
- "attend/<int:event_id>/" : Marks the logged-in user as attending a specific event.
- "unattend/<int:event_id>/" : Marks the logged-in user as not attending a specific event.
- "attended-events/" : Displays the events attended by the logged-in user.
"""

from . import views

app_name = "events"

urlpatterns = [
    path("", views.event_listing, name="event-listing"),
    path("<int:event_id>/", views.event_detail, name="event-detail"),
    path("add-event/", views.add_event, name="add-event"),
    path("my-events/", views.my_events, name="my-events"),
    path("update-event/<int:pk>/", views.update_event, name="update-event"),
    path("delete-event/<int:pk>/", views.delete_event, name="delete-event"),
    path("attend/<int:event_id>/", views.attend_event, name="attend-event"),
    path("unattend/<int:event_id>/", views.unattend_event, name="unattend-event"),
    path("attended-events/", views.attended_events, name="attended-events"),
]
