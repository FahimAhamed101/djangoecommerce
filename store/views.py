from django.shortcuts import render,get_object_or_404
from . models import Category,Product
# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'home.html',context)

def list_categories(request,category_slug=None):
    category = get_object_or_404(Product,slug=category_slug)
    products = Product.objects.filter(slug=category)
    context = {
        'products':products,
        'category':category,
    }
    return render(request,'list_categories.html',context)
def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}

def product_info(request,product_slug):
    product = get_object_or_404(Product,slug=product_slug)
    context = {
        'product':product,
    }
    return render(request,'product_info.html',context)