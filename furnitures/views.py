from decimal import Decimal

from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .models import Product


def main(request):
    return render(request, 'main.html')


def furnitures(request):
    products = Product.objects.filter(available=True, stock__gt=0)
    return render(request, 'furnitures.html', {'products': products})


@require_POST
def add_to_cart(request, product_id):
    try:
        product = Product.objects.get(pk=product_id, available=True, stock__gt=0)
    except Product.DoesNotExist:
        raise Http404('Furniture item not found')

    cart = request.session.get('cart', {})
    key = str(product_id)
    cart[key] = min(int(cart.get(key, 0)) + 1, product.stock, 99)
    request.session['cart'] = cart
    messages.success(request, 'Item added to your cart.')
    return redirect('cart')


def cart(request):
    saved_cart = request.session.get('cart', {})
    items = []
    total = Decimal('0.00')

    products = Product.objects.in_bulk(saved_cart.keys())
    for product_id, saved_quantity in saved_cart.items():
        product = products.get(int(product_id))
        if product is None:
            continue
        quantity = int(saved_quantity)
        if quantity < 1:
            continue
        line_total = product.price * quantity
        items.append({
            'product': product,
            'quantity': quantity,
            'line_total': line_total,
        })
        total += line_total

    return render(request, 'cart.html', {'items': items, 'total': total})


@require_POST
def update_cart_item(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404('Furniture item not found')

    cart_items = request.session.get('cart', {})
    key = str(product_id)
    try:
        quantity = int(request.POST.get('quantity', '1'))
    except (TypeError, ValueError):
        quantity = 1

    if quantity < 1:
        cart_items.pop(key, None)
    elif product.stock > 0:
        cart_items[key] = min(quantity, product.stock, 99)
    else:
        cart_items.pop(key, None)

    request.session['cart'] = cart_items
    return redirect('cart')


@require_POST
def remove_from_cart(request, product_id):
    cart_items = request.session.get('cart', {})
    cart_items.pop(str(product_id), None)
    request.session['cart'] = cart_items
    return redirect('cart')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
