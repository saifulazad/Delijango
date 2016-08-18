from carton.cart import Cart
import simplejson as json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
# import json
from products.models import Product


def add(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=request.POST.get('id'))
    cart.add(product, price=product.price, quantity=request.POST.get('qty'))
    recent_product = {
        'name': product.productName,
        'image': product.image.url,
        'price': product.price,
        'total': cart.total,
        'items': cart.count,
    }
    return HttpResponse(
        json.dumps(recent_product,use_decimal=True),
        content_type="application/json"
    )
    # return HttpResponse(recent_product)


def remove(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=request.GET.get('product_id'))
    cart.remove(product)
    return HttpResponse(cart.total)


def show(request):
    return render(request, 'shopping/show-cart.html')
