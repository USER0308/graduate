from django.conf.urls import include, url
from .views import deploy, test_connection

urlpatterns = [
    url(r'^$', deploy),
    url(r'test_connection/$', test_connection)
]