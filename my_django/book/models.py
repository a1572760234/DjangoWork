from django.db import models

# Create your models here.

'''

3.改变表名:
    默认表名是:子应用名_类名 都是小写
    修改表名:
'''

class BookInfo(models.Model):
    name = models.CharField(max_length=10,unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'   #修改表名
        verbose_name = '书籍管理' #通过admin站点使用


class PeopleInfo(models.Model):
    #定义一个有序字典作为枚举
    GENDER_CHOICE = [
        (1,'man'),   
        (2,'woman'),
    ]
    name = models.CharField(max_length=20,unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE,default=1)
    description = models.CharField(max_length=100,null=True)
    is_delete = models.BooleanField(default=False)

    #外键的级联操作
    #此处书籍是主表,人物是从表,
    #从表数据根据主表而变化,主表删除一条数据,从表的数据,
    #,
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

