from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from xhtml2pdf import pisa
from payment.models import CartItem, Booking
from decimal import Decimal  # Import Decimal for working with monetary values

def receipt(request):
    last_cart_item = CartItem.objects.last()  # Get the last CartItem object
    last_booking = Booking.objects.last()  # Get the last CartItem object

    if last_cart_item:
        product_price = last_cart_item.product.price
        cartItem_quantity = last_cart_item.quantity
        tax = product_price * Decimal('0.07')
    else:
        product_price = Decimal('0.00')
        cartItem_quantity = 0
        tax = Decimal('0.00')

    template_path = 'bill/receipt.html'
    context = {
    'name': last_booking.name if last_booking else '',
    'email': last_booking.email if last_booking else '',
    'number': last_booking.number if last_booking else '',
    'address': last_booking.address if last_booking else '',
    'pincode': last_booking.pincode if last_booking else '',
    'country': last_booking.country if last_booking else '',
    'id': last_booking.id if last_booking else '',
    'date': last_booking.date if last_booking else '',
    'product': last_cart_item.product if last_cart_item.product else '',
    'cartItem_quantity': cartItem_quantity,
    'product_price': product_price,
    'tax': tax,
    'sub_total': (product_price * cartItem_quantity),
    'total_with_tax': (product_price * cartItem_quantity) + tax,
}

    # Rest of your code for rendering the template and passing context

    

    template = get_template(template_path)
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="{last_booking.name}_bill.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)
    return response