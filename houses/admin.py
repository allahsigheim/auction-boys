from django.contrib import admin

# Register your models here.
from .models import House, Flatlet, Extra_Images_House
admin.site.register(House)

admin.site.register(Flatlet)
admin.site.register(Extra_Images_House)