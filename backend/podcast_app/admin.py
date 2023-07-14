from django.contrib import admin

from .models import Language, Author, Podcast, Episode

admin.site.register(Language)
admin.site.register(Author)
admin.site.register(Podcast)
admin.site.register(Episode)