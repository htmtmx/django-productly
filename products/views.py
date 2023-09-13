from django.shortcuts import render
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
    product = Product.objects.get(id=product_id)
    return render(request, 'detail.html', context={
        'product': product
    })