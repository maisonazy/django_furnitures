from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('furnitures/',views.furnitures,name='furnitures'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:product_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
]
