from django.http import HttpResponse
from django.shortcuts import render

from carton.cart import Cart
from products.models import Product

#
# def add(request, quantity, product_id= None):
#     cart = Cart(request.session)
#     product = Product.objects.get(id=product_id)
#     print(quantity)
#     cart.add(product, price=product.price, quantity=quantity)
#     return HttpResponse("Added")
#
# def remove(request, product_id= None):
#     cart = Cart(request.session)
#     product = Product.objects.get(id=product_id)
#     cart.remove(product)
#     return HttpResponse("Removed")
#
#
# def show(request):
#     return render(request, 'shopping/show-cart.html')



def add(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=request.POST.get('id'))
    cart.add(product, price=product.price, quantity=request.POST.get('qty'))
    return HttpResponse("Added")

def remove(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=request.GET.get('product_id'))
    cart.remove(product)
    return HttpResponse("Removed")


def show(request):
    return render(request, 'shopping/show-cart.html')
