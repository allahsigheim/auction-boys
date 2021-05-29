from django.shortcuts import render
from home.models import Agent
agents = Agent.objects.all()

# Create your views here.
from .models import Townhouse
def index(request):
    townhouses = Townhouse.objects.all()
    return render(request, 'townhouses/index.html', {'townhouses': townhouses})
    
def detail(request, townhouses_id):
    try:
        townhouse = Townhouse.objects.get(pk=townhouses_id)
    except Townhouse.DoesNotExist:
        raise Http404("Property does not exist")
    return render(request, 'townhouses/detail.html', {'townhouse': townhouse, 'agents':agents})