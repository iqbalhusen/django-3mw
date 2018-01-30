from django.contrib import admin
from django.urls import path, re_path

from apps.main import views


urlpatterns = [
    re_path('^$', views.home),
    path('admin/', admin.site.urls)
]
