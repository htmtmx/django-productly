from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()

    return render(
        request, 'index.html', context={
            'products': products
        }
    )


def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'detail.html', context={
        'product': product
    })