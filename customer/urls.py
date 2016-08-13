from django.conf.urls import url
from django.conf.urls import handler400, handler403, handler404, handler500

from . import views

# handler403 = 'views.permission_denied'
# handler404 = 'views.page_not_found'
# handler500 = 'views.server_error'



urlpatterns = [
    # ex: /customers
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
]
handler404 = 'views.bad_request'
