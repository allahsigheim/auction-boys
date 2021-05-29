from django.shortcuts import render
from django.http import Http404
# Create your views here.
from .models import House, Flatlet
from home.models import Agent
agents = Agent.objects.all()



def index(request):
    houses = House.objects.all()
    return render(request, 'houses/index.html', {'houses': houses})

def detail(request, house_id):
    try:
        house = House.objects.get(pk=house_id)
    except House.DoesNotExist:
        raise Http404("Property does not exist")
    return render(request, 'houses/detail.html', {'house': house, 'agents':agents})