from django.shortcuts import get_object_or_404
from products.models import Product, ProductCategory


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """
    
    cart = request.session.get('cart', {})


    cart_items = []
    total = 0
    product_count = 0
    """
    For loop ensures the user uses the same template for each product added to the cart.
    Key value pairs returned for cart_items, total & product_count.
    """

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})

    return {
        'cart_items': cart_items, 
        'total': total,    
        'product_count': product_count,
        'categories': ProductCategory.objects.all(),
    }
