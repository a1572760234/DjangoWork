from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest,HttpResponse

def index(request,urlFir,urlNex):

    return HttpResponse(f'Request OK,{urlFir}/{urlNex}')

def register(request):
    # json数据无法通过request.POST获取数据
    # print(request.POST,request)
    # {
    #     "name": "itcast",
    #     "age": 10
    # } <class 'str'>
    #json形式的字符串，可以转换成python字典通过 json模块

    import json
    body = request.body.decode()
    body_dict = json.loads(body)
    print(body_dict,type(body_dict))
    print(request.META)
    return  HttpResponse(request)

def set_cookie(request):
    # 1.获取查询字符串数据
    username = request.GET.get("username")
    # 2.服务器设置cookie信息
    response = HttpResponse('set_cookie')
    return response
    pass

def get_cookit(request):
    return HttpResponse('get_cookie')

def json(request):
    pass