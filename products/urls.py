from django.conf.urls import url, include
from .views import all_products, product_details


urlpatterns = [
    url(r"^products", all_products, name="all_products"),
    url(
        r"^product-details/(?P<id>\d+)",
        product_details,
        name="product_details",
    ),
]
