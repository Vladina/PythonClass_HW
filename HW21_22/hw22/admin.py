from django.contrib import admin

from hw21.models import Person
from hw22.models import MusicBand, Album, Track

# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'profession')
    fields = ('profession',)
    readonly_fields = ('age',)

@admin.register(MusicBand)
class MusicBandAdmin(admin.ModelAdmin):
    list_display = ('name', 'creation_year', 'style')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'issue_year', 'band')

@admin.register(Track)
class AlbumTrack(admin.ModelAdmin):
    list_display = ('name', 'track_length', 'album')