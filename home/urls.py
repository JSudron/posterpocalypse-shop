from django.conf.urls import url, include
from home.views import about


urlpatterns = [
    url(r'^about/', about, name="about"),
]
