from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils import timezone
from .models import Product
import sweetify


"""
Create product views
"""


def all_products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }

    page = request.GET.get("page", 1)
    products = products.order_by("name")
    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(
        request, 
        "products.html", 
        context,
        {
            "products": products,
        },
    )


"""
View products in a category
"""


def categories(request):
    categories = Product.objects.all()
    context = {
        'categories': categories
    }

    page = request.GET.get("page", 1)
    products = products.order_by("name")
    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", context)


""" 
View to show specific product details, per product 
"""


def product_details(request, id):
    products = get_object_or_404(Product, id=id)
    context = {
        'product': products
    }
    return render(request, "productdetail.html", context)
