from django.shortcuts import render
from django.urls.conf import path

from cart.forms import CartAddProductForm
from .models import Category, Product, News, Discount, Topics, Movie, Brand
# Create your views here.


def index(request):
    return render(request, 'main/index.html', {})


def catalog(request, category_slug=None):
    category=None
    if category_slug:
        category = Category.objects.filter(slug=category_slug)[0]
        products = Product.objects.filter(available=True, category=category)
    else:
        products = Product.objects.filter(available=True)
    return render(request, 'main/catalog.html', {
        'products': products,
        'category': category,
    })


def service(request):
    return render(request, 'main/service.html', {})


def discount(request):
    discount = Discount.objects.all().order_by('created')[::-1]
    return render(request, 'main/discount.html', {
        'discount_list': discount,
    })


def delivery(request):
    return render(request, 'main/delivery.html', {})


def brand(request):
    brand = Brand.objects.filter(available=True)
    return render(request, 'main/brand.html', {
        'brand_list': brand,
    })


def news(request):
    news = News.objects.all().order_by('created')[::-1]
    return render(request, 'main/news.html', {
        'news_list': news,
    })


def topics(request):
    topics = Topics.objects.all().order_by('created')[::-1]
    return render(request, 'main/topics.html', {
        'topics_list': topics,
    })


def movie(request):
    movie = Movie.objects.all().order_by('created')[::-1]
    return render(request, 'main/movie.html', {
        'movie_list': movie,
    })


def contacts(request):
    return render(request, 'main/contacts.html', {})


def product_detail(request, id, slug):
    cart_product_form = CartAddProductForm()
    products = Product.objects.all().order_by('created')[:3:-1]
    news = News.objects.all().order_by('created')[:3:-1]
    product = Product.objects.filter(slug=slug, id=id)[0]
    return render(request, 'main/product/product.html', {
        'product_list': products,
        'product': product,
        'news_list': news,
        'cart_product_form': cart_product_form,
    })

def search(request):
    query = request.GET.get('query')
    products = Product.objects.filter(name__icontains=query)
    return render(request, 'main/search.html', {
        'products': products
    })
