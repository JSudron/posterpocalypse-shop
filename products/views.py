from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Product, ProductCategory


def all_products(request):
    """
    Allows user to view all products but also search by name & filter by category
    """

    products = Product.objects.all()
    name = request.GET.get("q")
    category_id = request.GET.get("category_id")
    if category_id:
        products = products.filter(category_id=category_id)

    if name:
        products = products.filter(name__icontains=name)
    
    page = request.GET.get("page")
    products = products.order_by("name")

    """
    Renders the product list with pagination
    9 products per page
    """

    paginator = Paginator(products, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(
        request,
        "products.html",
        {
            "products": products,
            "categories": ProductCategory.objects.all(),
        },
    )


def product_details(request, id):
    """
    Displays the details of the chosen product
    """

    product = Product.objects.get(id=id)
    return render(request, "product-details.html", {"product": product})