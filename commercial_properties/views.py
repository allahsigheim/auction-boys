from django.shortcuts import render
from home.models import Agent
agents = Agent.objects.all()

# Create your views here.
from .models import Commercial
def index(request):
    commercial_properties = Commercial.objects.all()
    return render(request, 'commercial_properties/index.html', {'coms': commercial_properties})

def detail(request, commercial_id):
    try:
        commercial = Commercial.objects.get(pk=commercial_id)
    except Commercial.DoesNotExist:
        raise Http404("Property does not exist")
    return render(request, 'commercial_properties/detail.html', {'coms': commercial, 'agents':agents})