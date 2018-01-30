from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.db.models import Sum, Avg
from django.db import connection

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
        with connection.cursor() as cursor:
            cursor.execute("SELECT AVG(a) FROM main_site WHERE category_id = %s;", [site_category.id])
            row = cursor.fetchone()
            avg_a = row[0]

            cursor.execute("SELECT AVG(b) FROM main_site WHERE category_id = %s;", [site_category.id])
            row = cursor.fetchone()
            avg_b = row[0]

            site_category_data.append({
                'name': site_category.name,
                'a_value': round(avg_a, 2) if avg_a else avg_a,
                'b_value': round(avg_b, 2) if avg_b else avg_b
            })

    return render(request, 'main/summary.html', {'site_category_data': site_category_data})
