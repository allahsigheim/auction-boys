from django.shortcuts import render
import json
from django.shortcuts import *
from django.template import RequestContext
import locale
locale.setlocale(locale.LC_ALL, 'en_US')


# Create your views here.
from .models import Apartment, Apartment_Bid
from django.db.models import Max
from django.contrib.auth.models import User
from home.models import Agent
agents = Agent.objects.all()
from .forms import BidAomount

def index(request):
    apartments = Apartment.objects.all()
    return render(request, 'apartments/index.html', {'apartments': apartments})

def detail(request, apartment_id):
    try:
        apartment = Apartment.objects.get(pk=apartment_id)
    except Apartment.DoesNotExist:
        raise Http404("Property does not exist")
    return render(request, 'apartments/detail.html', {'apartment': apartment, 'agents':agents})


def bid(request, apartment_id):
    try:
        apartment = Apartment.objects.get(pk=apartment_id)
    except Apartment.DoesNotExist:
        raise Http404("Property does not exist")
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print('post found')
        # create a form instance and populate it with data from the request:
        form = BidAomount(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # check for max price 
            try:
                max_price = Apartment_Bid.objects.filter(apartment=apartment).aggregate(Max('amount'))['amount__max']
                if max_price < form.cleaned_data['price']:
                    ab = Apartment_Bid(amount = form.cleaned_data['price'], apartment = apartment, user = request.user)
                    ab.save()
                
                top_bids = (Apartment_Bid.objects
                    .filter(apartment=apartment)
                     .order_by('-amount')
                     .values_list('amount', flat=True)
                     .distinct())
                lis = sorted([i for i in top_bids])[-6:-1]
                lis = [locale.format("%d", i, grouping=True) for i in lis]
                

            except:
                ab = Apartment_Bid(amount = form.cleaned_data['price'], apartment = apartment, user = request.user)
                ab.save()
            if max_price:
                return render(request, 'apartments/bid.html', {'apartment': apartment, 'agents':agents, 'form': form, 'max_price': locale.format("%d", max_price, grouping=True), 'min': max_price+10000, 'top': lis})
            else:
                return render(request, 'apartments/bid.html', {'apartment': apartment, 'agents':agents, 'form': form, 'max_price': max_price})


    # if a GET (or any other method) we'll create a blank form
    else:
        try:
            
            max_price = Apartment_Bid.objects.filter(apartment=apartment).aggregate(Max('amount'))['amount__max']
            form = BidAomount()
            
            
            top_bids = (Apartment_Bid.objects
                    .filter(apartment=apartment)
                    .order_by('-amount')
                    .values_list('amount', flat=True)
                    .distinct())
            lis = sorted([i for i in top_bids])[-6:-1]
            lis = [locale.format("%d", i, grouping=True) for i in lis]
            if max_price:
                return render(request, 'apartments/bid.html', {'apartment': apartment, 'agents':agents, 'form': form, 'max_price': locale.format("%d", max_price, grouping=True), 'min': max_price+10000, 'top': lis})
            else:
                return render(request, 'apartments/bid.html', {'apartment': apartment, 'agents':agents, 'form': form, 'max_price': max_price})
        except:
            form = BidAomount()
            return render(request, 'apartments/bid.html', {'apartment': apartment, 'agents':agents, 'form': form})

