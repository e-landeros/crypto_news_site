from django.shortcuts import render
import requests
import json

def home(request):
    #crypto news
    api_news_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    news = json.loads(api_news_request.content)

    #crypto price data
    api_price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTCS,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD')
    price = json.loads(api_price_request.content)
    

    context = {
        'news':news,
        'price':price,
    }

    return render(request, 'home.html', context)

def prices(request):
    if request.method == 'POST':
        quote = request.POST['quote'].upper()

        crypto_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+ quote +'&tsyms=USD')
        crypto = json.loads(crypto_request.content)

        context = {
            'quote':quote,
            'crypto': crypto,
        }
        
        return render(request, 'prices.html', context)

    else:
        return render(request, 'prices.html', {})