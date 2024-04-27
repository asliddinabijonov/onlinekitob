from django.contrib import admin
from .models import *


@admin.register(Bolim)
class BolimAdmin(admin.ModelAdmin):
    list_display = ('nomi',)


@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'muallif')



@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ('ism',)
