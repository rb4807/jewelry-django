from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem,Booking
from explore.models import Product
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic.base import TemplateView
import stripe

# add to cart

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user, ordered=False)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart')

# cart

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user, ordered=False)
    context = {'cart_items': cart_items}
    return render(request, 'payment/cart.html', context)


# increase quantity

@login_required
def increase_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

# decrease quantity

@login_required
def decrease_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('cart')

# remove from cart

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

# booking

@login_required
def booking(request):
    if request.method == 'POST':
        name = request.POST[ 'name']
        email = request.POST[ 'email']
        number = request.POST[ 'number']
        country = request.POST[ 'country']
        city = request.POST[ 'city']
        pincode = request.POST[ 'pincode']
        address = request.POST[ 'address']

        booking = Booking(name=name, number=number, email=email, country=country, city=city, pincode=pincode, address=address)
        booking.save()

        return render(request, 'payment/payment_method.html')
    else:
        return render(request, 'payment/booking.html')

def success(request):
    return render(request, 'payment/success.html')


# payment

class payment(TemplateView):
    template_name = 'payment\payment.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

stripe.api_key = settings.STRIPE_SECRET_KEY
def charge(request):
    publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, 'payment/charge.html', {'key': publishable_key})

    if request.method == 'POST':
        try:
            token = request.POST['stripeToken']
            charge = stripe.Charge.create(
                amount=81385,
                currency='inr',
                description='Payment Gateway',
                source=token,
            )
            return render(request, 'payment/charge.html')
        except stripe.error.CardError as e:
            return render(request, 'payment/error.html', {'error': e})
        except Exception as e:
            return render(request, 'payment/error.html', {'error': e})
    return redirect('payment')

def error(request):
    return render(request, 'payment/error.html')