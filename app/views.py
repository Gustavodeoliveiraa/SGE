import json
from django.shortcuts import render
from . import metrics


def home(request):
    daily_sales_date = metrics.get_daily_sales_date()
    daily_sales_quantity_date = metrics.get_daily_sales_quantity_data()

    context = {
        'daily_sales_date': json.dumps(daily_sales_date),
        'daily_sales_quantity_date': json.dumps(daily_sales_quantity_date)
    }

    return render(request, 'home.html', context)
