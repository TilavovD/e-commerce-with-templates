from django.shortcuts import render
from .models import Product

# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store.html', context)


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')