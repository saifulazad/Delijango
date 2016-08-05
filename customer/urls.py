from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /customers
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^products/', views.single_product, name='single_product'),
]