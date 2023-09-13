from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all().values()
    print(products)
    # return HttpResponse(products[0].name + " " + str(products[0].created_at))
    return JsonResponse(list(products), safe=False)