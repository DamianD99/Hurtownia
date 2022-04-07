from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST


from hurtownia.models import Produkty
from .cart import Cart
from .forms import CartAddProductForm, KupnoAddressForm
from .models import KupnoAddress


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Produkty, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Produkty, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'override': True})
    return render(request, 'cart/cart.html', {'cart': cart})

def zakup(request):
    zakup = KupnoAddress.objects.all()

    if request.method == 'POST':
        form = KupnoAddressForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('cart:zakup')
    else:
        form = KupnoAddressForm()
    context = {
        'zakup': zakup,
        'form': form,
    }
    return render(request, "cart/zakup.html", context)
# Create your views here.
