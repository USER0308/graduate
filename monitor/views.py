from django.shortcuts import render, render_to_response, HttpResponse
import json
import os
from monitor.client import networking
# Create your views here.

def monitor(request):
    return render(request, 'monitor.html')

def getHostInfo(request):
    if request.method == 'POST':
        total_host = []
        hostjson = 'hostinfo.json'
        if os.path.exists(hostjson):
            with open(hostjson) as fr:
                total_host = json.load(fr)
             #   print(type(json.dumps(total_host)))
        return HttpResponse(json.dumps({'total_host': total_host}))

def info(request):
    return render(request, 'admin_organization.html')

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

def getBlockchainInfo(request):
    if request.method == 'GET':
        #res = networking('getBlockchainInfo')
        # res = ''
        blockchain_info = {
            'ordererNum': 1,
            'organizationNum': 2,
            'peerNum': 2,
            'caNum': 1,
            'couchdbNum': 5
        }
        response = {'code': '200', 'blockchain': blockchain_info}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))



def admin_docker(request):
    return render(request, 'admin_docker.html')

def admin_test(request):
    return render(request, 'admin_test.html')

def admin_querychain(request):
    return render(request, 'admin_querychain.html')