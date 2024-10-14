from django.contrib import admin
from . import models
from simple_history.admin import SimpleHistoryAdmin
from simple_history import signals
admin.site.register(models.LunaAI)
admin.site.register(models.Producer)
admin.site.register(models.Song)
admin.site.register(models.Genre)

@admin.register(models.History)
class HistoryAdmin(SimpleHistoryAdmin):
    list_display = ['song', 'usuario', 'date']
