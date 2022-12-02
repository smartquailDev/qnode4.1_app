from .cart_c import Cart_C


def cart_c(request):
    return {'cart_c': Cart_C(request)}
