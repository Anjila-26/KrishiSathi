from django.shortcuts import render
from .models import Vegetables

def vegetable_list(request):
    query = request.GET.get('q')
    query_product = request.GET.get('product')
    query_date = request.GET.get('date')

    if query_product:
        vegetables = Vegetables.objects.filter(product__icontains=query_product)
    elif query_date:
        vegetables = Vegetables.objects.filter(date=query_date)
    else:
        # Retrieve only the latest date data
        latest_date = Vegetables.objects.latest('date').date
        vegetables = Vegetables.objects.filter(date=latest_date)

    if query:
        vegetables = vegetables.filter(product__icontains=query)

    return render(request, 'vegetable.html', {'vegetables': vegetables})
