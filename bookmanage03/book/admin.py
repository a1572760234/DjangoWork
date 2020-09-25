from django.contrib import admin

# Register your models here.
from book.models import BookInfo,PeopleInfo

#注册人物和书籍models
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)