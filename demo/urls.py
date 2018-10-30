"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# import users.urls
import users.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls', namespace='users')),  # 添加应用的路由
    # 也可以导入urls模块, 直接传递应用的urls模块
    # url(r'^users/', include(users.urls))
    # 也可将工程的全部路由信息都定义在主路由文件中，子应用不再设置urls.py(不常用)
    # url(r'^users/index/$', users.views.index)
    url(r'', include('reqresp.urls', namespace='reqresp')),
    url(r'', include('classview.urls')),
]
