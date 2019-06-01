# encoding: utf-8
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
        # print(len(block_hash))
        # hash_hex = []
        # i = 0
        # while i < (len(block_hash)-1):
        #     if block_hash[i] == '\\':
        #         if block_hash[i+1].isdigit():
        #             num = int('' + block_hash[i+1] + block_hash[i+2] + block_hash[i+3], 8)
        #             num = bytes([num])
        #             hash_hex.append(num)
        #             i += 4
        #         else:
        #             hash_hex.append(block_hash[i+1])
        #             i += 2
        #     else:
        #         hash_hex.append(block_hash[i])
        #         i += 1
        # block = bytes(hash_hex)
        # hash_hex = block.decode(encoding='utf-8')
        # print(hash_hex)

        # print(type(hash_hex[0]))
        #hash_hex = '\004%}c0K\227\303\026\254Y\2734L\374\347\006\032\234\3548\'\322\250\013\002\266\240\007\231=\036'
        res = networking('blockHash' + block_hash)
        #res = 'not foundend'
        if res == 'not foundend':
            res = '找不到相关信息'
        response = {'code': '200', 'msg': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))

def queryBlockByTxid(request):
    if request.method == 'POST':
        txid = request.POST.get('txid')
        print(txid)
        res = networking('blockTxid' + txid)
        if res == 'not foundend':
            res = '找不到相关信息'
        response = {'code': '200', 'msg': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))

def queryTransactionByTxid(request):
    if request.method == 'POST':
        txid = request.POST.get('txid')
        print(txid)
        res = networking('transactionId'+txid)
        if res == 'not foundend':
            res = '找不到相关信息'
        # print(res)
        response = {'code': '200', 'msg': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))

def queryInstalledChaincode(request):
    if request.method == 'POST':
        res = networking('installed')
        # print(res)
        res = res[:-3]
        res = res.replace('\n', '<br/>&emsp;')
        print(res)
        response = {'code': '200', 'msg': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))

def queryInstantiatedChaincode(request):
    if request.method == 'POST':
        res = networking('instantiated')
        res = res[: -3]
        res = res.replace('\n', '<br/>&emsp;')
        response = {'code': '200', 'msg': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))

def queryChannel(request):
    if request.method == 'POST':
        res = networking('queryChannel')
        res = res[: -3]
        res = res.replace('\n', '<br/>&emsp;')
        response = {'code': '200', 'msg': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))

def getChannelConfig(request):
    if request.method == 'POST':
        res = networking('channelConfig')
        res = res[:5000]
        # res = res.replace('\n', '<br/>')
        response = {'code': '200', 'msg': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))

def getInfo(request):
    if request.method == 'POST':
        res = networking('queryInfo')
        res = res[:-3]
        res = res.replace('\n', '<br/>&emsp;')
        print(res)
        response = {'code': '200', 'msg': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))

def getBlockchainInfo(request):
    if request.method == 'GET':
        res = networking('blockchainInfo')
        res = res[:-3]
        print(res)
        info = json.loads(res)
        print(info)
        blockchain_info = {
            'ordererNum': info['orderer_num'],
            'organizationNum': info['org_num'],
            'peerNum': info['peer_num'],
            'caNum': info['ca_num'],
            'couchdbNum': info['couchdb_num']
        }
        response = {'code': '200', 'blockchain': blockchain_info}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))

def operateChaincode(request):
    if request.method == 'GET':
        return render(request, 'admin_chaincodeOperate.html')

def queryChaincode(request):
    if request.method == 'POST':
        args = request.POST.get('args')
        res = networking('queryArgsChaincode' + args)
        res_list = res.split('->')
        line = res_list[-2]
        # print(line)
        line = line[-55:-40]
        line = line.split(' ')
        line = line[2]
        # print(line)
        # res = res[:-100]
        # index = res.find("Query Result:")
        # res = res[index: 4]
        response = {'code': '200', 'queryResult': line}
        return HttpResponse(json.dumps(response))

def invokeChaincode(request):
    if request.method == 'POST':
        args = request.POST.get('args')
        print(args)
        res = networking('invokeArgsChaincode' + args)
        res = res[-121:-50]
        response = {'code': '200', 'invokeResult': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '200', 'invokeResult': "invoke successful"}
    return HttpResponse(json.dumps(response))

def admin_docker(request):
    return render(request, 'admin_docker.html')

def admin_test(request):
    return render(request, 'admin_test.html')

def admin_querychain(request):
    return render(request, 'admin_querychain.html')

def admin_blockchainInfo(request):
    return render(request, 'admin_blockchainInfo.html')

def admin_network_stop(request):
    if request.method == 'POST':
        res = networking('stop')
        response = {'code': '200', 'msg': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))

def admin_network_clear(request):
    if request.method == 'POST':
        res = networking('clear')
        response = {'code': '200', 'msg': res}
        return HttpResponse(json.dumps(response))
    response = {'code': '403', 'msg': 'forbidden'}
    return HttpResponse(json.dumps(response))

def get_os_info(request):
    host_info = ''
    res = networking('getOSInfo')
    if request.method == 'GET':
        # host_info = {
        #     'os': 'GNU/Linux Ubuntu16.04 x86_64',
        #     'ip': '192.168.10.100',
        #     'domainName': '192.168.10.100',
        #     'dockerVersion': '17.05.0',
        #     'totalContainer': '4',
        #     'activeContainer': '8'
        # }
        # print(res)
        res = res[:-3]
        host_info = json.loads(res)
        response = {'code': '200', 'msg': host_info}
        return HttpResponse(json.dumps(response))
    else:
        return HttpResponse("error")

def get_docker_info(request):
    if request.method == 'GET':
        res = networking('getDockerInfo')
        res = res[:-4]
        # res = res.replace(' ', '*')
        # print(res)
        res_lines = res.split('\n')

        containers = []
        for line in res_lines:
            words = line.split('\t')
            # print(words)
            container = {
                'id': words[0],
                'image': words[1],
                'command': words[2],
                'create_time': words[3],
                'status': words[4],
                'name': words[5]
            }
            containers.append(container)
        print(containers)

        response = {'code': '200', 'msg': containers}
        return HttpResponse(json.dumps(response))