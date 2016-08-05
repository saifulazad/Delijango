from django.http import Http404
from django.shortcuts import render

from products.models import Product


# Create your views here.

def product_detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'product_details.html', {'product': product})