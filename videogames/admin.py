from django.contrib import admin
from . import models


class VideogameAdmin(admin.ModelAdmin):
    fields = ('owner', 'title', 'platform', 'formato', 'release_date', 'front_cover', 'description')
    list_display = ('__str__', 'slug', 'owner')

admin.site.register(models.Videogame, VideogameAdmin)
admin.site.register(models.Platform)
admin.site.register(models.Format)