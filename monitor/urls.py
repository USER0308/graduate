from django.conf.urls import include, url
from .views import monitor, queryBlockByHash, queryBlockByTxid, queryTransactionByTxid, queryInstalledChaincode, queryInstantiatedChaincode, queryChannel, getChannelConfig, getInfo, info
urlpatterns = [
    url(r'^$', monitor),
    url(r'info/$', info),
    url(r'queryBlockByHash/$', queryBlockByHash),
    url(r'queryBlockByTxid/$', queryBlockByTxid),
    url(r'queryTransactionByTxid/$', queryTransactionByTxid),
    url(r'queryInstalledChaincode/$', queryInstalledChaincode),
    url(r'queryInstantiatedChaincode/$', queryInstantiatedChaincode),
    url(r'queryChannel/$', queryChannel),
    url(r'getChannelConfig/$', getChannelConfig),
    url(r'getInfo/$', getInfo),
]