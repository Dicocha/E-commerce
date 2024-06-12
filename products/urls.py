from django.urls import path
from .views import ProductListView
from products import views

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('<str:id>', views.filter, name='filter'),
    path('<str:text>', views.search, name='search'),
    path('add/', views.add, name='add'),
    path('add-to-cart/<int:pk>/<int:quantity>', views.add_to_cart, name='add_to_cart'),
    path('<int:pk>/', views.detail, name='detail'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
]