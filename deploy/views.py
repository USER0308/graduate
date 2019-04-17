#! encoding=utf-8
from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse,render_to_response
import paramiko
import json

def deploy(request):
    if request.method == 'GET':
        return render(request, 'deploy.html')
    elif request.method == 'POST':
        orderer_num = request.POST.get('ordererNum')
        org_num = request.POST.get('organizationNum')
        peer_num = request.POST.get('peerNum')
        ca_num = request.POST.get('caNum')
        couchdb_num = request.POST.get('couchdbNum')
        print(orderer_num)
        print(org_num)
        print(peer_num)
        print(ca_num)
        print(couchdb_num)
        response = {'code': '200', 'msg': 'deploy ok'}
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

        response = {'code': '200', 'msg': 'OK'}
        ssh.close()
        return HttpResponse(json.dumps(response))