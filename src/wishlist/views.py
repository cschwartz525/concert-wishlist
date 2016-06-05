from django.shortcuts import render

import datetime
import json
import requests

# Create your views here.
def home(request):
    title = 'Concert Wishlist'

    page = 1
    response = requests.get('https://api.seatgeek.com/2/events?venue.city=New%20York&page=' + str(page))
    data = json.loads(response.text)
    events = parseEventData(data)

    context = {
        'title': title,
        'events': events
    }

    return render(request, 'home.html', context)


def parseEventData(data):
    events = []
    for item in data['events']:
        dt = datetime.datetime.strptime(item['datetime_local'], "%Y-%m-%dT%H:%M:%S")
        event = {
            'title': item['title'],
            'venue': item['venue']['name'],
            'datetime': dt.strftime('%Y-%m-%d %I:%M %p')
        }
        events.append(event)
    return events
