from django.db import models

# Create your models here.
# 书籍信息
class BookInfo(models.Model):
    #设置字段信息
    name = models.CharField(max_length=20,verbose_name='书籍名称')
    pub_date = models.DateField(verbose_name='发布日期',null=True)
    readcount = models.IntegerField(default=0,verbose_name='阅读量')
    commentcount = models.IntegerField(default=0,verbose_name='评论量')
    is_delete = models.BooleanField(default=False,verbose_name='是否逻辑删除')

    class Meta:
        db_table='bookinfo' #设置表名
        verbose_name = '图书' #设置显示信息,in admin
        verbose_name_plural = verbose_name

    # 设置返回信息
    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    #设置字段枚举
    GENDER_CHOICES=(
        (0,'man'),
        (1,'woman')
    )

    #设置字段信息
    name = models.CharField(max_length=20,verbose_name='人物名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES,default=0,verbose_name='性别')
    description = models.CharField(max_length=200,null=True,verbose_name='描述信息')
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name='图书')
    is_delete = models.BooleanField(default=False,verbose_name='是否逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name='人物信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.name