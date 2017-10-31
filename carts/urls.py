from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_goods/$', views.add_goods, name='add_goods'),
    url(r'^del_cart_goods/$', views.del_cart_goods, name='del_cart_goods'),
    url(r'^update_goods/$', views.update_goods, name='update_goods'),
]