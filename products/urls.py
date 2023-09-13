from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:product_id>", views.detail, name="product_detail"),
    path("add_product", views.add_product, name="add_product")
]
