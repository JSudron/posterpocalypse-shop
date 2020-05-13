from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from products.models import Product
from cart.models import Cart, CartItem


def view_cart(request):
    """
    Displays the cart contents page
    """

    return render(request, "cart.html")


def add_to_cart(request, id):
    """
    Add specified product to the cart stored in session.
    Update total price of all products in cart.
    Creates or updates user cart, which is later loaded
    after login.
    """

    quantity = int(request.POST.get("quantity") or 1)

    product = Product.objects.get(id=id)
    if quantity > product.quantity:
        messages.error(request, f"Only {product.quantity} availible")

        return redirect(reverse("all_products"))

    cart = request.session.get("cart", {})

    if not cart.get(id):
        cart[id] = cart.get(id, quantity)
    else:
        cart[id] += quantity

    request.session["cart"] = cart
    total = round(float(product.price) * quantity, 2)
    if request.session.get("total"):
        request.session["total"] += total

    else:
        request.session["total"] = total
    if request.user.is_authenticated():
        user_cart, created = Cart.objects.get_or_create(user=request.user)
        item = CartItem.objects.filter(cart=user_cart, product_id=id).first()
        if item:
            item.quntity = cart[id]
            item.save()
        else:
            CartItem.objects.create(
                cart=user_cart, product_id=id, quantity=cart[id]
            )

    return redirect(reverse("all_products"))


def adjust_cart(request, id):
    """
    Adjust the quantity of the product or delete selected item from cart.
    """

    quantity = request.POST.get("quantity")
    if not quantity:
        messages.error(request, "Choose quantity")
        return redirect(reverse("view_cart"))
    quantity = int(quantity)
    if quantity < 1:
        messages.error(request, "Quantity must be higher then 0")
        return redirect(reverse("view_cart"))
    product = Product.objects.get(id=id)
    if quantity > product.quantity:
        messages.error(request, f"Only {product.quantity} available")

        return redirect(reverse("view_cart"))
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
