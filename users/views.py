from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def index(request):
    """
    视图
    :param request: 用于接收request对象
    :return: httpResponse() 必须返回httpResponse对象
    """
    return HttpResponse("hello django!")


def say(request):
    """
    url(r'^users/', include('users.urls', namespace='users'))
    url(r'^index/$', views.index, name='index')
    因为之前有为views.index命名,并且为users.urls定义了命名空间,
    这里可以使用reverse()反解析到index的路径
    :param request:
    :return:
    """
    url = reverse('users:index')  # 返回 /users/index/
    print(url)

    return HttpResponse('say hello')
