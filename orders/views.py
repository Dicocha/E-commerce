from django.shortcuts import get_object_or_404, redirect, render
from .models import Order

def cart(request):
    orders = Order.objects.all()
    total_amount = 0

    for order in orders:
        total_amount = order.subtotal

    context = {
        'orders': orders,
        'total_amount': total_amount,
    }
    return render(request, 'orders/cart.html', context)

def delete(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == 'POST':
        order.delete()
    
    return redirect('orders:cart')
