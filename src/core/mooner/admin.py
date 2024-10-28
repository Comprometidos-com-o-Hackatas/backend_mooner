from django.contrib import admin
from . import models
from simple_history.admin import SimpleHistoryAdmin
from simple_history import signals
admin.site.register(models.LunaAI)
admin.site.register(models.Song)
admin.site.register(models.Genre)
admin.site.register(models.Playlist)
admin.site.register(models.Album)
admin.site.register(models.Community)
admin.site.register(models.CommunityPosts)
admin.site.register(models.LikedSong)
admin.site.register(models.Following)

@admin.register(models.History)
class HistoryAdmin(SimpleHistoryAdmin):
    list_display = ['song', 'usuario', 'date']
