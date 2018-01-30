from django.contrib import admin

from .models import *


@admin.register(SiteCategory)
class SiteCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'date', 'a', 'b')
