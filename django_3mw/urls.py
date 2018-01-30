from django.contrib import admin
from django.urls import path, re_path

from apps.main import views


urlpatterns = [
    re_path('^$', views.home),
    path('sites/', views.home, name='sites'),
    path('sites/<int:site_category_id>/', views.site_category_details, name='site-category-details'),
    path('admin/', admin.site.urls)
]
