

# Register your models here.
# incidents/admin.py
from django.contrib import admin
from .models import SafetyIncident

admin.site.register(SafetyIncident)
