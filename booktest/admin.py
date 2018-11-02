from django.contrib import admin
from booktest.models import BookInfo, HeroInfo
# Register your models here.


admin.site.site_header = '图书管理'  # 设置网站页头
admin.site.site_title = '图书'  # 设置页面标题
admin.site.index_title = '后台管理'  # 设置首页标语


# 关联对象(一对多)
# 然后要在BookInfoAdmin中增加属性inlines = [BookStackedInline]
class BookStackedInline(admin.TabularInline):
    model = HeroInfo  # 指定关联的子对象
    extra = 2  # 可以额外再编辑2个子对象


# 需要创建超级管理员 --python manage.py createsuperuser
# 管理员登陆页面 http://127.0.0.1:8000/admin/
# 注册模型类方法1:
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['btitle', 'bpub_date', 'image']

    # 编辑页面展示
    # 显示内容&顺序
    # fields = ['btitle', 'bpub_date']
    # 分组显示(和上面的fields选一个设置)
    fieldsets = (
        ('基本', {'fields': ['btitle']}),
        ('高级', {'fields': ['bpub_date', 'bread', 'image']})
    )
    # 关联对象(一对多)
    inlines = [BookStackedInline]

admin.site.register(BookInfo, BookInfoAdmin)


# 方法2:模型类上使用装饰器
@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    # 每页中显示多少条数据
    list_per_page = 10
    # "操作选项"的位置
    actions_on_top = True
    actions_on_bottom = False
    # 列表中的列的显示
    list_display = ['hname', 'hgender', 'hcomment', 'gender', 'parent']
    # 将方法作为列
    # 需要再模型类中定义方法,如
    # def gender(self):
    #     if self.hgender == 0:
    #         gen = '男'
    #     else:
    #         gen = '女'
    #     return gen
    # 指定排序依据
    # gender.admin_order_field = 'hgender'
    # 指定列标题
    # gender.short_description='男/女'

    # 右侧栏过滤器
    list_filter = ['hbook', 'hgender']

    # 搜索框
    search_fields = ['hname']