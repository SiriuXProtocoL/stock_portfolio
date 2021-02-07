from django.shortcuts import render
#import from the internet
import requests
#parse it
import json

# Create your views here.
def home(request):

    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_183750c8ece6430f84f747bfb19be397")
    
    try:
        api = json.loads(api_request.content)

    #if there api does not return anything as json
    except Exception as e:
        api = "Error..."


    return render(request, 'home.html', {'api': api})

def about(request):

    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_183750c8ece6430f84f747bfb19be397")
    
    try:
        api = json.loads(api_request.content)

    #if there api does not return anything as json
    except Exception as e:
        api = "Error..."

    return render(request, 'about.html', {'api': api})
