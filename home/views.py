from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import ProductCategory
from products.views import all_products


def index(request, *args, **kwargs):
    """A view that displays the index page"""
    return render(request, "index.html", 
        {
            "home": "index",
            "categories": ProductCategory.objects.all(),
        },
    )


def about(request, *args, **kwargs):
    """A view that displays the about page"""
    return render(request, "about.html", {"home": "about"})
