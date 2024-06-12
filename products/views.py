from django.views.generic import ListView
from orders.models import Order
from products.forms import ProductForm
from .models import Product
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.admin.views.decorators import staff_member_required

class ProductListView(ListView):
    model = Product
    template_name = 'products/home.html'
    context_object_name = 'products'

def search(request):
    text = request.GET.get('text')

    if text:
        products = Product.objects.filter(name__icontains=text)
    else:
        products = Product.objects.none()
    
    return render(request, 'products/search_results.html', {'products': products})

def filter(request, id):
    # Define a dictionary mapping filter keys to filter functions
    filters = {
        'ase': ascending_name,
        'dec': descending_name,
        'barato': ascending_price,
        'caro': descending_price,
    }

    # Get the filter function corresponding to the given attribute
    filter_func = filters.get(id)

    if filter_func:
        products = filter_func()

    else:
        products = Product.objects.all()

    return render(request, 'products/home.html', {'products': products})

def ascending_name():
    return Product.objects.all().order_by('name')

def descending_name():
    return Product.objects.all().order_by('-name')

def ascending_price():
    return Product.objects.all().order_by('price')

def descending_price():
    return Product.objects.all().order_by('-price')


# Only can create articles the admins.
@staff_member_required
def detail(request, pk):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'products/detail.html', {'product': product, 'form': form})

@staff_member_required
def add(request):
    if request.method == 'GET':
        return render(request, 'products/add.html', {
            'form': ProductForm
        })
    
    elif request.method == 'POST':
        try:
            form = ProductForm(request.POST, request.FILES)
            new_product = form.save(commit = False)
            new_product.user = request.user
            if form.is_valid():
                form.save()
                return redirect('products:home')

        except ValueError:
            return render(request, 'products/add.html', {
                'form': ProductForm,
                'error': "Please provide valid data"
            })
        
def add_to_cart(request, pk, quantity):
    product = get_object_or_404(Product, pk=pk)

    # Check if the user already has an active order, create one if not
    order, created = Order.objects.get_or_create(user=request.user, product=product, defaults={'quantity': quantity})

    if not created:
        order.quantity += int(quantity)
        order.save()

    return redirect('products:home')

@staff_member_required
def update(request, pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect('products:home')

@staff_member_required
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        product.delete()

    return redirect('products:home')