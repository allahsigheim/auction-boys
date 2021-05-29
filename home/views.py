from django.shortcuts import render
from .models import Agent
# Create your views here.
def index(request):
    agent = Agent.objects.get(pk=2)
    print(agent)
    return render(request, 'home/index.html', {'agent': agent})

def guide(request):
    return render(request, 'home/guide.html')