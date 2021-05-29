from django.contrib import admin

# Register your models here.
from .models import Industrial_Property, Crane, Extra_Images_Industrial_Property
admin.site.register(Industrial_Property)
admin.site.register(Crane)
admin.site.register(Extra_Images_Industrial_Property)
