from django.contrib import admin
from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'foto']
    raw_id_fields = ['user']

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Book_Genre)
admin.site.register(User_Reading)