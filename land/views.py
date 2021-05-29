from django.shortcuts import render
from home.models import Agent
agents = Agent.objects.all()

# Create your views here.
from .models import Land
def index(request):
    land = Land.objects.all()
    return render(request, 'land/index.html', {'land': land})

def detail(request, land_id):
    try:
        land = Land.objects.get(pk=land_id)
    except Land.DoesNotExist:
        raise Http404("Property does not exist")
    return render(request, 'land/detail.html', {'ld': land, 'agents':agents})