from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from main.models import Product
from main.task import send_beat_email, send_spam_email
from shop import settings
from .cart import Cart
from .forms import CartAddProductForm, OrderForm
from django.core.mail import send_mail
from django.views.generic import CreateView

from .models import Order


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


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart.html', {'cart': cart})


class OrderCreate(CreateView):
    model = Order
    template_name = 'order.html'
    form_class = OrderForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        email = 'awequamy@gmail.com'
        send_spam_email.delay(email)
        return super().form_valid(form)
