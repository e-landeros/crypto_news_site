from django.shortcuts import render
import requests
import json

def home(request):
    #crypto news
    api_news_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    news = json.loads(api_news_request.content)

    #crypto price data
    api_price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP&tsyms=USD,EUR')
    price = json.loads(api_price_request.content)
    

    context = {
        'news':news,
        'price':price,
    }

    return render(request, 'home.html', context)