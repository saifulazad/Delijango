from django.conf.urls import url

from cart import views

urlpatterns = [
    # ex: /customers
    url(r'^(?P<product_id>[0-9]+)/(?P<quantity>[0-9]+)$', views.add_to_cart, name='add_to_cart'),
]