from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^query/', views.query),
    url(r'^$', views.index, name='index'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^list/(\d+)/(\d+)/$', views.list, name='list'),
]