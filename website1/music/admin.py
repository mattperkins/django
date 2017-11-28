from django.contrib import admin
from . models import Album
from . models import Song

# register (Music) Album and Song Models to admin dashboard
admin.site.register(Album)
admin.site.register(Song)
