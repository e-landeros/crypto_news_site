from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)

    context = {
        'api':api
    }

    return render(request, 'home.html', context)