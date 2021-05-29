from django.contrib import admin

# Register your models here.
from .models import Land, Extra_Images_Land 
admin.site.register(Land)
admin.site.register(Extra_Images_Land)