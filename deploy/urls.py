from django.conf.urls import include, url
from .views import deploy, test_connection, install_software, pull_image, config, yaml_up, create_channel, join_channel, install_chaincode, instantiate_chaincode

urlpatterns = [
    url(r'^$', deploy),
    url(r'install_software/$',install_software),
    url(r'pull_image/$',pull_image),
    url(r'config/$', config),
    url(r'yaml_up/$',yaml_up),
    url(r'create_channel/$',create_channel),
    url(r'join_channel/$',join_channel),
    url(r'install_chaincode/$',install_chaincode),
    url(r'instantiate_chaincode/$',instantiate_chaincode),
    url(r'test_connection/$', test_connection)
]