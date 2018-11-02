from django.contrib import admin
from booktest.models import BookInfo, HeroInfo
# Register your models here.

# 需要创建超级管理员 --python manage.py createsuperuser
# 管理员登陆页面 http://127.0.0.1:8000/admin/
# 注册模型类方法1:
admin.site.register(BookInfo)


# 方法2:模型类上使用装饰器
@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    pass