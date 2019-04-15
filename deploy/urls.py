from django.conf.urls import include, url
from .views import deploy

urlpatterns = [
    url(r'^$', deploy),
    url(r'^deploy/$', deploy),
]