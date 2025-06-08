from django.shortcuts import render
from django.utils import timezone
from .models import Event

def countdown_timer(request):
    event = Event.objects.first()  # Get the first event
    if event:
        time_remaining = event.event_date - timezone.now()
        hours = time_remaining.seconds // 3600
        minutes = (time_remaining.seconds % 3600) // 60
        seconds = time_remaining.seconds % 60
        data = {
            'name': event.name,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        }
    else:
        data = {
            'name': "No Event",
            'hours': 0,
            'minutes': 0,
            'seconds': 0
        }
    return render(request, 'myapp.html', {'data': data})
