from django.contrib import admin
from .models import Platos

@admin.register(Platos)
class PlatosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'procedencia',)
    fields = ('nombre', 'procedencia',)
    search_fields = ('nombre',)