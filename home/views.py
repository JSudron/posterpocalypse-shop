from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import ProductCategory
from products.views import all_products

def index(request):
    """
    Displays the index page
    """

    return render(request, "index.html")

def about(request):
    """
    Displays the about page
    """
    
    return render(request, "about.html")


def contact(request):
    """
    Displays the about page
    """
    
    return render(request, "contact.html")
