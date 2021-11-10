from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    # добавить сюда вс те пути , которые мы пропишем в новом файл
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('service/', views.service, name='service'),
    path('discount/', views.discount, name='discount'),
    path('delivery/', views.delivery, name='delivery'),
    path('brand/', views.brand, name='brand'),
    path('news/', views.news, name='news'),
    path('topics/', views.topics, name='topics'),
    path('movie/', views.movie, name='movie'),
    path('contacts/', views.contacts, name='contacts'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.catalog,
        name='catalog_by_category'),
    path('search/', views.search, name='search'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
]
