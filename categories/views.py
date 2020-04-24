from django.shortcuts import render
from products.models import Product


def product_filter(request, category):
    products = Product.objects.filter(category=the_category)
    return render(request, "products.html", {"products": products})
