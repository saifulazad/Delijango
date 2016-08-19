from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /customers
    url(r'^(?P<product_id>[0-9]+)$', views.product_detail, name='product_detail'),
    url(r'^search/$', views.search, name='product_search'),
]
