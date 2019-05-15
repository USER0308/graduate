from django.conf.urls import include, url
from .views import monitor, queryBlockByHash, queryBlockByTxid, queryTransactionByTxid, queryInstalledChaincode, queryInstantiatedChaincode, queryChannel, getChannelConfig, getInfo, getHostInfo, info
from .views import admin_docker, admin_test, admin_querychain, getBlockchainInfo, admin_blockchainInfo, operateChaincode, queryChaincode, invokeChaincode
urlpatterns = [
    url(r'^$', monitor),
    url(r'getHostInfo/$', getHostInfo),
    url(r'info/$', info),
    url(r'queryBlockByHash/$', queryBlockByHash),
    url(r'queryBlockByTxid/$', queryBlockByTxid),
    url(r'queryTransactionByTxid/$', queryTransactionByTxid),
    url(r'queryInstalledChaincode/$', queryInstalledChaincode),
    url(r'queryInstantiatedChaincode/$', queryInstantiatedChaincode),
    url(r'queryChannel/$', queryChannel),
    url(r'getChannelConfig/$', getChannelConfig),
    url(r'getInfo/$', getInfo),
    url(r'admin_docker/$', admin_docker),
    url(r'admin_reset/$', admin_test),
    url(r'admin_querychain/$', admin_querychain),
    url(r'getBlockchainInfo/$', getBlockchainInfo),
    url(r'admin_blockchainInfo/$', admin_blockchainInfo),
    url(r'admin_operateChaincode/$', operateChaincode),
    url(r'admin_queryChaincode/$', queryChaincode),
    url(r'admin_invokeChaincode/$', invokeChaincode),
]