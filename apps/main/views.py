from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.db.models import Sum, Avg

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
    site_category_data = []

    for site_category in SiteCategory.objects.all():
        sum_a_dict = Site.objects.filter(category=site_category).aggregate(Sum('a'))
        sum_a = sum_a_dict[next(iter(sum_a_dict))]

        sum_b_dict = Site.objects.filter(category=site_category).aggregate(Sum('b'))
        sum_b = sum_b_dict[next(iter(sum_b_dict))]

        site_category_data.append({
            'name': site_category.name,
            'a_value': sum_a,
            'b_value': sum_b
        })

    return render(request, 'main/summary.html', {'site_category_data': site_category_data})


def summary_avg(request):
    site_category_data = []

    for site_category in SiteCategory.objects.all():
        avg_a_dict = Site.objects.filter(category=site_category).aggregate(Avg('a'))
        avg_a = avg_a_dict[next(iter(avg_a_dict))]

        avg_b_dict = Site.objects.filter(category=site_category).aggregate(Avg('b'))
        avg_b = avg_b_dict[next(iter(avg_b_dict))]

        site_category_data.append({
            'name': site_category.name,
            'a_value': avg_a,
            'b_value': avg_b
        })

    return render(request, 'main/summary.html', {'site_category_data': site_category_data})
