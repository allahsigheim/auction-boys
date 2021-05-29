from django.shortcuts import render
from home.models import Agent
agents = Agent.objects.all()

# Create your views here.
from .models import Sectional_Industrial_Property
def index(request):
    sectional_industrial_properties = Sectional_Industrial_Property.objects.all()
    return render(request, 'sectional_industrial_properties/index.html', {'sectional_industrial_properties': sectional_industrial_properties})

def detail(request, sectional_industrial_properties_id):
    try:
        sectional_industrial_property = Sectional_Industrial_Property.objects.get(pk=sectional_industrial_properties_id)
    except Sectional_Industrial_Property.DoesNotExist:
        raise Http404("Property does not exist")
    return render(request, 'sectional_industrial_properties/detail.html', {'sip': sectional_industrial_property, 'agents':agents})