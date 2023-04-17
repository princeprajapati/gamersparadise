from accounts.models import CartItems

def cart_count(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItems.objects.filter(cart__is_paid=False, cart__user=request.user).count()
    return {'cart_count': cart_count}
