from django.shortcuts import render

# Create your views here.
from django.http import *

def index(request):
    return HttpResponse('ok')

def userRequest(request,request1_id,request2_id):
    return JsonResponse({'request1_id':request1_id,'request2_id':request2_id})