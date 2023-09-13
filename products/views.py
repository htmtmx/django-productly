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