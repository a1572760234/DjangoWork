from django.shortcuts import render

# Create your views here.
from django.http import *

def index(request):
    return HttpResponse('ok')

def userRequest(request,request1_id,request2_id):
    return JsonResponse({'request1_id':request1_id,'request2_id':request2_id})

def cookie(request):
    #设置cookie函数
    response = HttpResponse('request ok')
    response.set_cookie('testcookie','cookievalue',max_age=3600)
    response.set_cookie('testcookie2', 'cookievalue2',max_age=3600)
    print(request.COOKIES.get('testcookie'),request.COOKIES.get('testcookie2'))
    #删除cookie
    # response.delete_cookie('testcookie')
    # response.delete_cookie('testcookie2')
    return response