from django.shortcuts import render, redirect
#import from the internet
import requests
#parse it
import json
#accessing models
from .models import stock_db
#create a form file with this calss
from .forms import StockForm
#for pop up messages
from django.contrib import messages

# Create your views here.
def home(request):

    if request.method == "POST":

        #From the form input name field
        ticker = request.POST['ticker_symbol']

        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_183750c8ece6430f84f747bfb19be397")
    
        try:
            api = json.loads(api_request.content)

        #if there api does not return anything as json
        except Exception as e:
            api = "Error..."
        
        return render(request, 'home.html', {'api': api})

    
    else:
        return render(request, 'home.html', {'ticker': "Enter a ticker Symbol above..."})

def about(request):

    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_183750c8ece6430f84f747bfb19be397")
    
    try:
        api = json.loads(api_request.content)

    #if there api does not return anything as json
    except Exception as e:
        api = "Error..."

    return render(request, 'about.html', {'api': api})

def add_stock(request):

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request,("Stock has been Added!"))
            return redirect('add_stock')

    else:
        ticker = stock_db.objects.all()
        return render(request, 'add_stock.html', {"ticker": ticker})
