from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import F
from explore.models import Product

def sort_products(request):
    # Get sorting parameter (e.g., 'low_to_high' or 'high_to_low') from the request
    sorting_param = request.GET.get('sorting_param')

    # Determine the order by parameter based on the sorting option
    order_by_param = 'price'  # Default: Sort by price low to high
    if sorting_param == 'high_to_low':
        order_by_param = F('price').desc()

    # Sort the products based on the selected parameter
    products = Product.objects.all().order_by(order_by_param)

    # Serialize the sorted products and return as JSON
    serialized_products = [{'name': product.name, 'price': str(product.price)} for product in products]
    return JsonResponse({'products': serialized_products})

