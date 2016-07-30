from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /customers
    url(r'^$', views.index, name='index'),

]