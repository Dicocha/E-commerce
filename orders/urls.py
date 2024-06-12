from django.urls import path
from orders import views

app_name = 'orders'

urlpatterns = [
    path('', views.cart, name='cart'),
    path('delete/<int:pk>', views.delete, name='delete')
]
