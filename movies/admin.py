from django.contrib import admin
from .models import *


# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    list_display = ('title', 'number_in_stock', 'rating')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
