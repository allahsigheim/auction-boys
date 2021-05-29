from django.contrib import admin

# Register your models here.
from .models import Commercial, Extra_Images_Commercial
admin.site.register(Commercial)
admin.site.register(Extra_Images_Commercial)