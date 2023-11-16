from django.urls import path
from . import views

urlpatterns = [
    path("", views.products, name="products"),
    path(
        "<int:product_id>/",
        views.product_information,
        name="product_information",
    ),
    path("add/", views.add_product, name="add_product"),
    path("edit/", views.edit_product, name="edit_product"),
    path(
        "delete/<int:product_id>/", views.delete_product, name="delete_product"
    ),
]
