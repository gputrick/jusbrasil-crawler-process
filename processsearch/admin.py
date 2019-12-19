from django.contrib import admin
from .models import Process, Move

class ProcessList(admin.ModelAdmin):
    list_display = ('id', 'process', 'classe', 'subject', 'distribuition', 'control', 'judge', 'action_value')
    list_display_links = ('id', 'process', 'classe', 'subject', 'distribuition', 'control', 'judge', 'action_value')
    search_fields = ('id', 'process', 'classe', 'subject', 'distribuition', 'control', 'judge', 'action_value')
    list_filter = ('id', 'process', 'classe', 'subject', 'distribuition', 'control', 'judge', 'action_value')
    list_per_page = 10

admin.site.register(Process, ProcessList)
