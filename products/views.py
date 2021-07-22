from django.shortcuts import render

from  products.models import Product, ProductCategory
# Create your views here.

def index(request):
    context = {
        'title': 'Geekshop',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {'title': 'Geekshop - Каталог', 'categories': ProductCategory.objects.all()}
    if category_id:
        context['products'] = Product.objects.filter(category_id=category_id)
    else:
        context['products'] = Product.objects.all()
    return render(request, 'products/products.html', context)