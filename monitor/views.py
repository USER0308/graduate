from django.shortcuts import render, render_to_response

# Create your views here.

def monitor(request):
    return render_to_response('monitor.html')