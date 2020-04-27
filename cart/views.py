from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from products.models import Product
import sweetify


def view_cart(request):

    """A View that renders the cart contents page"""

    return render(request, "cart.html", {"disable_footer": True})


def add_to_cart(request, id):
    """
    Add quantity of specified
    product to the cart stored in session.
    Update total price of all products in cart.
    Creates or updates user cart, which is later loaded
    after login.
    """

    quantity = int(request.POST.get("quantity") or 1)

    product = Product.objects.get(id=id)
    if quantity > product.quantity:
        sweetify.error(request, f"Only {product.quantity} availible")

        return redirect(reverse("index"))
    cart = request.session.get("cart", {})

    previous_quantity = cart[id]
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session["cart"] = cart

    total = round(float(product.price) * quantity, 2)
    if request.session.get("total"):
        request.session["total"] += total
        request.session["total"] -= round(
            float(product.price) * previous_quantity, 2
        )
    else:
        request.session["total"] = total
    if request.user.is_authenticated():
        cart_object, created = Cart.objects.get_or_create(user=request.user)
        item = CartItem.objects.filter(cart=cart_object, product_id=id).first()
        if item:
            item.quantity = cart[id]
            item.save()
        else:
            CartItem.objects.create(
                cart=cart_object, product_id=id, quantity=cart[id]
            )
    return redirect(reverse("view_cart"))


def cart_item_delete(request, item_id):

    """
    User can remove items from the shopping
    cart. 
    """

    if request.method == "POST":
        if request.user.is_authenticated():
            cart_object, created = Cart.objects.get_or_create(
                user=request.user
            )
            item = CartItem.objects.filter(
                cart=cart_object, product_id=item_id
            ).first()
            if item:
                item.delete()
        cart = request.session.get("cart")
        if cart and cart.get(item_id):
            cart.pop(item_id)
            request.session["cart"] = cart

    return redirect(reverse("view_cart"))

    
