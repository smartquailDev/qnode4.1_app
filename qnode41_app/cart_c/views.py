from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from services.models import Product
from .cart_c import Cart_C
from .forms import Cart_C_AddProductForm, Apply_C_ApplyForm


def cart_detail(request):
    cart_c = Cart_C(request)
    for item in cart_c:
            item['update_quantity_form'] = Cart_C_AddProductForm(
                              initial={'quantity': item['quantity'],
                              'update': True})
    apply_c_apply_form = Apply_C_ApplyForm()

    return render(request, 'cart_c/detail.html', {'cart_c': cart_c, 'apply_c_apply_form':apply_c_apply_form})
