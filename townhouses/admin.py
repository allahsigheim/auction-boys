from django.contrib import admin

# Register your models here.
from .models import Townhouse, Extra_Images_Townhouse
admin.site.register(Townhouse)
admin.site.register(Extra_Images_Townhouse)