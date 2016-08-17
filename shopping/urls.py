from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /customers
    # url(r'^add/(?P<product_id>[0-9]+)/(?P<quantity>[0-9]+)/$', views.add, name='shopping-cart-add'),
    # url(r'^remove/(?P<product_id>[0-9]+)/$', views.remove, name='shopping-cart-remove'),
    # url(r'^show/$', views.show, name='shopping-cart-show'),

    url(r'^add/$', views.add, name='shopping-cart-add'),
    url(r'^remove/$', views.remove, name='shopping-cart-remove'),
    url(r'^show/$', views.show, name='shopping-cart-show'),

]


