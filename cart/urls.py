from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    # добавить сюда вс те пути , которые мы пропишем в новом файл
    path('', views.cart, name='cart'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
    url(r'^clear/$', views.cart_clear, name='cart_clear'),
]