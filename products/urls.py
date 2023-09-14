from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.index, name="products"),
    path("<int:product_id>", views.detail, name="product_detail"),
    path("add_product", views.add_product, name="add_product")
]
