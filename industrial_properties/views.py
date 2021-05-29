from django.shortcuts import render
from home.models import Agent
agents = Agent.objects.all()

# Create your views here.
from .models import Industrial_Property
def index(request):
    industrial_properties = Industrial_Property.objects.all()
    return render(request, 'industrial_properties/index.html', {'industrial_properties': industrial_properties})

def detail(request, industrial_properties_id):
    try:
        industrial_property = Industrial_Property.objects.get(pk=industrial_properties_id)
    except Industrial_Property.DoesNotExist:
        raise Http404("Property does not exist")
    return render(request, 'industrial_properties/detail.html', {'industrial_properties': industrial_property, 'agents':agents})