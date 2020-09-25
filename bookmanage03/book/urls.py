from django.urls import path
from django.contrib import admin
from book.views import index,register,json
from django.urls.converters import register_converter

#提取url制作路由
class MobileConverter:
    regex = '1[3-9]\d{9}'

    def to_python(self,value):
        return value

register_converter(MobileConverter,'phone')
urlpatterns = [
    #转换器，<数据类型:请求参数>/<数据类型:请求参数>
    #转换器会对请求参数进行正则验证
    path('index/',index),
    path('<int:urlFir>/<phone:urlNex>',index),
    path('',admin.site.urls),
    path('register/',register),
    path('json/',json)
]