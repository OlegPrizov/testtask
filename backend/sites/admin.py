from django.contrib import admin
from .models import Site

class SiteAdmin(admin.ModelAdmin):
    list_display = ('creator', 'name', 'url',)
    search_fields = ('creator', 'name', 'url',)
    list_filter = ('creator',)

admin.site.register(Site, SiteAdmin)