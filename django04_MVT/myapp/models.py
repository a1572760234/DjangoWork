from django.db import models

# Create your models here.
class BookInfo(models.Model):
    #定义bookinfo表字段
    name = models.CharField(max_length=20,verbose_name='名称')
    pub_date = models.DateField(verbose_name='发布日期',null=True)
    readcount = models.IntegerField(default=0,verbose_name='阅读量')
    commentcount = models.IntegerField(default=0,verbose_name='评论量')
    is_delete = models.BooleanField(default=False,verbose_name='是否逻辑删除')

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '图书'
        verbose_name_plural='图书'

    def __str__(self):
        #定义查询返回值
        return self.name

class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        #定义gender字段所用枚举
        (0,'male'),
        (1,'female')
    )
    name = models.CharField(max_length=20,verbose_name='人物名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES,default=0,verbose_name='性别')
    description = models.CharField(max_length=200,null=True,verbose_name='描述信息')
    is_delete = models.BooleanField(default=False,verbose_name='是否逻辑删除')
    #关联外键主表：bookinfo
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name='图书')

    def __str__(self):
        #定义查询返回
        return self.name

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'
        verbose_name_plural = '人物信息'

