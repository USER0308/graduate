from django.conf.urls import include, url
from .views import monitor
urlpatterns = [
    url(r'^$', monitor),
]