from django.shortcuts import render

# Create your views here.
from apartments.models import Apartment
from commercial_properties.models import Commercial
from houses.models import House
from industrial_properties.models import Industrial_Property
from land.models import Land
from sectional_industrial_properties.models import Sectional_Industrial_Property
from townhouses.models import Townhouse

def index(request):
    apartments = Apartment.objects.all()
    commercial_properties = Commercial.objects.all()
    houses = House.objects.all()
    industrial_properties = Industrial_Property.objects.all()
    sectional_industrial_properties = Sectional_Industrial_Property.objects.all()
    land = Land.objects.all()
    townhouses = Townhouse.objects.all()
    return render(request, 'all/index.html', {
        'apartments': apartments, 
        'commercial_properties': commercial_properties, 
        'houses': houses, 
        'industrial_properties': industrial_properties, 
        'land': land, 
        'sectional_industrial_properties': sectional_industrial_properties, 
        'townhouses': townhouses, 
        })


        