from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import ProductForm 
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()

    return render(
        request, 'products.html', context={
            'products': products
        }
    )


def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'detail.html', context={
        'product': product
    })

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/products")
    else:
        form = ProductForm()
    return render(
        request, 'add_product.html', {
        'product_form': form})