from django.conf.urls import url, include

from booktest import views_new

from rest_framework import routers
# 1） 创建router对象，并注册视图集
router = routers.SimpleRouter()
router.register(r'books', views_new.BookAPIView, base_name='book')
# 第一个参数:prefix 该视图集的url前缀
# 第二个参数:viewset 对应哪个视图集
# 第三个参数:base_name 路由名字的前缀
# 如上述代码会形成的路由如下：
# ^books/$    name: book-list
# ^books/{pk}/$   name: book-detail

# 视图集中自定义的动作形成的路由:
# ^books/latest/$    name: book-latest

# 2）添加路由数据(两种方法)

urlpatterns = [
    url(r'^', include(router.urls)),
]

# 或者:
# urlpatterns += router.urls  # 向列表追加数据的方法
