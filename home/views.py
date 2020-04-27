from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import ProductCategory
from products.views import all_products


def about(request, *args, **kwargs):
    """A view that displays the about page"""
    return render(request, "about.html", {"home": "about"})
