from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('alter/<product_id>/', views.alter_cart, name='alter_cart'),
    path('empty/', views.empty_cart, name='empty_cart'),
]
