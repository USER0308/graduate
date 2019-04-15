from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from deploy.utils import build_network, software_dl, template

def deploy(request):
    orderer_num = 0
    org_num = 2
    peer_num = 2
    ca_num = 1
    if request.method == 'GET':
        return HttpResponse("getting deployment args")
    elif request.method == 'POST':
        orderer_num = request.POST.get('orderer_num') , 0
        org_num = request.POST.get('org_num'), 2
        peer_num = request.POST.get('peer_num'), 2
        ca_num = request.POST.get('ca_num'), 1
        couchdb_num = request.POST.get('couchdb_num'), 1

        software_dl.install_all()
        software_dl.download_img('x86-64-1.0.0')
        software_dl.download_ca('x86-64-1.0.0')
        software_dl.download_binary()

        template.configtx_gen(orderer_num=orderer_num, org_num=org_num, peer_num=peer_num, ca_num=ca_num, couchdb_num=couchdb_num)
        template.crypto_config_gen(orderer_num=orderer_num, org_num=org_num, peer_num=peer_num)
        template.docker_compose_gen(orderer_num=orderer_num, org_num=org_num, peer_num=peer_num, ca_num=ca_num, couchdb_num=couchdb_num)

        build_network.generate()
        build_network.network_up()

        return HttpResponse("deploying finished")