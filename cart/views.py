from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from main.models import Product
from .forms import CartAddProductForm
from django.views.decorators.http import require_POST
# Create your views here.


def cart(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {
        'cart': cart
    })


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart')

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                update_quantity=cd['update'])
    return redirect('cart:cart')

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart')
