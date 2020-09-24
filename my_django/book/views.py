from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from book.models import BookInfo,PeopleInfo

# Create your views here.
def index(request):
    books = BookInfo.objects.all()
    print(books)
    return HttpResponse('index')



###############增加数据
book = BookInfo(
    name = 'Django',
    pub_date = '2000-1-1',
    readcount = 10
)
book.save()

#方式2
BookInfo.objects.create(
    name = '测试开发入门',
    pub_date = '2020-1-1',
    readcount = 100
)

####################修改数据
# 方式1 save()
book = BookInfo.objects.get(id=6)
book.name = '运维开发入门'
book.save()

# 方式2 update
BookInfo.objects.filter(name='运维开发入门').update(name='嵌入式开发入门')

##################删除数据
# 方式1 模型类对象.delete
book = BookInfo.objects.get(name='嵌入式开发入门')
book.delete()


##################查询
# 方式1,get对象查询,查询单一结果,如果不存在则抛出模型类DoesNotExist异常
# 方式2,all查询多个结果
# 方式3,count查询结果数量
BookInfo.objects.get(id=1)
BookInfo.objects.all()
BookInfo.objects.all().count()

################条件查询
# filter过滤出多个结果
# exclude排除掉符合条件剩下的结果
# get过滤单一结果
# book = BookInfo.objects.filter(id__contains
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)