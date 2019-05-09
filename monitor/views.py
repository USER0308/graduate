from django.shortcuts import render, render_to_response, HttpResponse
import json
from monitor.client import networking
# Create your views here.

def monitor(request):
    return render(request, 'monitor.html')

def info(request):
    return render(request, 'info.html')

def queryBlockByHash(request):
    if request.method == 'POST':
        block_hash = request.POST.get('hash')
        print(block_hash)
        res = networking('blockHash' + block_hash)
        print(res)
        response = {'code': '200', 'msg': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))

def queryBlockByTxid(request):
    if request.method == 'POST':
        txid = request.POST.get('txid')
        print(txid)
        res = networking('blockTxid' + txid)
        print(res)
        response = {'code': '200', 'msg': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))

def queryTransactionByTxid(request):
    if request.method == 'POST':
        txid = request.POST.get('txid')
        print(txid)
        res = networking('transactionId'+txid)
        print(res)
        response = {'code': '200', 'msg': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))

def queryInstalledChaincode(request):
    if request.method == 'POST':
        res = networking('installed')
        response = {'code': '200', 'msg': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))

def queryInstantiatedChaincode(request):
    if request.method == 'POST':
        res = networking('instantiated')
        response = {'code': '200', 'msg': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))

def queryChannel(request):
    if request.method == 'POST':
        res = networking('queryChannel')
        response = {'code': '200', 'msg': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))

def getChannelConfig(request):
    if request.method == 'POST':
        res = networking('channelConfig')
        response = {'code': '200', 'msg': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))

def getInfo(request):
    if request.method == 'POST':
        res = networking('queryInfo')
        response = {'code': '200', 'msg': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))