from django.shortcuts import render

from .models import *


def home(request):
    return render(request, 'main/home.html', {'site_categories': SiteCategory.objects.all()})


def site_category_details(request, site_category_id):
    print('site_category_id', site_category_id, type(site_category_id))
    return render(request, 'main/site_category_details.html')
