from django.shortcuts import render

from .forms import SearchForm

import datetime
import json
import requests
import urllib

# Create your views here.
def home(request):
    title = 'Concert Wishlist'
    form = SearchForm(request.POST or None)

    events = []

    if form.is_valid():
        form_param_key = form.cleaned_data.get('param_key')
        form_param_value = form.cleaned_data.get('param_value')
        form_page = form.cleaned_data.get('page')

        params = {
            'page': form_page,
            form_param_key: form_param_value,
        }

        url = 'https://api.seatgeek.com/2/events?%s' % (urllib.urlencode(params))
        response = requests.get(url)
        data = json.loads(response.text)
        events = parseEventData(data)

    context = {
        'title': title,
        'form': form,
        'events': events,
    }

    return render(request, 'home.html', context)

def parseEventData(data):
    events = []
    for item in data['events']:
        dt = datetime.datetime.strptime(item['datetime_local'], "%Y-%m-%dT%H:%M:%S")
        event = {
            'id': item['id'],
            'title': item['title'],
            'venue': item['venue']['name'],
            'datetime': dt.strftime('%Y-%m-%d %I:%M %p'),
        }
        events.append(event)
    return events

def event(request, eventId):
    title = 'Event'

    url = 'https://api.seatgeek.com/2/events/' + eventId
    response = requests.get(url)
    data = json.loads(response.text)

    dt = datetime.datetime.strptime(data['datetime_local'], "%Y-%m-%dT%H:%M:%S")
    event = {
        'id': data['id'],
        'title': data['title'],
        'venue': data['venue']['name'],
        'datetime': dt.strftime('%Y-%m-%d %I:%M %p'),
    }

    context = {
        'title': title,
        'event': event,
    }

    return render(request, 'event.html', context)
