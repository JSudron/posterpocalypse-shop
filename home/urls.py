from django.conf.urls import url, include
from home.views import index, about


urlpatterns = [
    url(r"^$", index, name="index"),
    url(r'^about/', about, name="about"),
]
