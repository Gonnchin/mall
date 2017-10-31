from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.user_info, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^order/$', views.user_order, name='order'),
    url(r'^address/$', views.user_address, name='address'),
    url(r'^register_handle/$', views.register_handle, name='register_handle'),
    url(r'^login_handle/$', views.login_handle, name='login_handle'),
    url(r'^check_exist/$', views.check_exist, name='check_exist'),
    url(r'^logoff/$', views.logoff, name='logoff'),
    url(r'^addr_handle/$', views.addr_handle, name='addr_handle'),
]