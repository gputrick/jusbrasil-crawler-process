from django.contrib import admin
from .models import Process, Move

class ProcessList(admin.ModelAdmin):
    list_display = ('id', 'process_number')
    list_display_links = ('id', 'process_number')
    search_fields = ('id', 'process_number')
    list_filter = ('id', 'process_number')
    list_per_page = 10

admin.site.register(Process, ProcessList)
