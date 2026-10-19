def cart_context(request):
    cart = request.session.get('cart', {})
    return {'cart_item_count': sum(int(quantity) for quantity in cart.values())}
