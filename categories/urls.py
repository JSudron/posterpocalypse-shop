from django.conf.urls import url, include
from .views import product_filter


urlpatterns = [
    url(r'(?P<category>\w+)/$', product_filter, name='product-filter'),
]
