#! encoding=utf-8
from django.shortcuts import render
from .client import networking
# Create your views here.
from django.shortcuts import HttpResponse,render_to_response
import paramiko
import json
import os.path

def deploy(request):
    if request.method == 'GET':
        return render(request, 'deploy.html')
    elif request.method == 'POST':
        orderer_num = request.POST.get('ordererNum')
        org_num = request.POST.get('organizationNum')
        peer_num = request.POST.get('peerNum')
        ca_num = request.POST.get('caNum')
        couchdb_num = request.POST.get('couchdbNum')
        info = {
            'orderer_num': orderer_num,
            'org_num': org_num,
            'peer_num': peer_num,
            'couchdb_num': couchdb_num,
            'ca_num': ca_num
        }
        info_str = json.dumps(info)
        networking('num'+info_str)
        # print(orderer_num)
        # print(org_num)
        # print(peer_num)
        # print(ca_num)
        # print(couchdb_num)
        #try except
        #networking('metadata'+'/'+orderer_num+'/'+org_num+'/'+peer_num+'/'+ca_num+'/'+couchdb_num)
        #networking('installSoftware')
        response = {'code': '200', 'msg': 'ok'}
        return HttpResponse(json.dumps(response))

def index(request):
    return render_to_response('index.html')

def test_connection(request):
    if request.method == 'POST':
        hostname = request.POST.get('ip')
        user = request.POST.get('user')
        password = request.POST.get('password')
        print(hostname)
        print(user)
        print(password)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname=hostname, port=22, username=user, password=password, allow_agent=False,look_for_keys=False, timeout=5)
        except Exception as e:
            print(e)
            response = {'code': '500', 'msg': 'timeout'}
            ssh.close()
            return HttpResponse(json.dumps(response))

        # 验证是否成功登录
        #写入本地
        total_host = []
        host_info = {
            'hostname': hostname,
            'user': user,
            'password': password
        }
        hostjson = 'hostinfo.json'
        if not os.path.exists(hostjson):
            print('not exists')
            total_host.append(host_info)
        else:
            print('exists')
            with open(hostjson) as fr:
                total_host = json.load(fr)
            flag = True
            for h in total_host:
                if h['hostname'] == host_info.get('hostname') and h['user'] == host_info.get('user'):
                    h['password'] = host_info.get('password')
                    flag = False
            if flag:
                total_host.append(host_info)

        with open(hostjson, "w") as fw:
            json.dump(total_host, fw)
            fw.close()

        response = {'code': '200', 'msg': 'OK'}
        ssh.close()
        return HttpResponse(json.dumps(response))

def install_software(request):
    # networking('software')
    # networking('binary')
    response = {'code': '200', 'msg': 'ok'}
    return HttpResponse(json.dumps(response))

def pull_image(request):
    # networking('image')
    response = {'code': '200', 'msg': 'ok'}
    return HttpResponse(json.dumps(response))

def config(request):
    networking('config')
    networking('material')
    networking('docker-compose')
    response = {'code': '200', 'msg': 'ok'}
    return HttpResponse(json.dumps(response))

def yaml_up(request):
    networking('build')
    response = {'code': '200', 'msg': 'ok'}
    return HttpResponse(json.dumps(response))

def create_channel(request):
    networking('createChannel')
    response = {'code': '200', 'msg': 'ok'}
    return HttpResponse(json.dumps(response))

def join_channel(request):
    networking('joinChannel')
    response = {'code': '200', 'msg': 'ok'}
    return HttpResponse(json.dumps(response))

def install_chaincode(request):
    networking('installChaincode')
    response = {'code': '200', 'msg': 'ok'}
    return HttpResponse(json.dumps(response))

def instantiate_chaincode(request):
    networking('instantiateChaincode')
    response = {'code': '200', 'msg': 'ok'}
    return HttpResponse(json.dumps(response))