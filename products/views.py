from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from products.models import Product


# Create your views here.

@login_required
def product_detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        products = Product.objects.all()
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    context = {
        'product': product,
        'products': products,
    }
    return render(request, 'product_details.html', context)


def search(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'product_search.html', context)
