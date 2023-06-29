from django.urls import path
from .views import cart, store, checkout

urlpatterns = [
    path('', store, name='store'),
    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
]