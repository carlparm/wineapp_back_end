from django.contrib import admin
from .models import Wine

# Register your models here.

# admin.site.register(Wine)

@admin.register(Wine)
class WineModel(admin.ModelAdmin):
    list_filter = ('name', 'vinyard', 'year', 'gwscore')
    list_display = ('name', 'vinyard', 'year', 'gwscore')
