from django.contrib import admin

# Register your models here.
from .models import Apartment, Apartment_Bid, Extra_Images_Apartment
admin.site.register(Apartment)
admin.site.register(Apartment_Bid)

admin.site.register(Extra_Images_Apartment)
