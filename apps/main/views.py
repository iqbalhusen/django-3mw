from django.shortcuts import render
from django.http import HttpResponseNotFound

from .models import *


def home(request):
    return render(request, 'main/home.html', {'site_categories': SiteCategory.objects.all()})


def site_category_details(request, site_category_id):
    try:
        site_category = SiteCategory.objects.get(id=site_category_id)
    except SiteCategory.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    context_dict = {
        'site_category_name': site_category.name,
        'sites': Site.objects.filter(category=site_category)
    }

    return render(request, 'main/site_category_details.html', context_dict)


def summary_sum(request):
    return render(request, 'main/summary_sum.html')


def summary_avg(request):
    return render(request, 'main/summary_avg.html')
