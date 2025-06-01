from django.contrib import admin

# Register your models here.
# principal/admin.py
from django.contrib import admin
from .models import PaginaInicial

admin.site.register(PaginaInicial)
