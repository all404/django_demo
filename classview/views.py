from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View


class RegisterView(View):
    """类视图: 处理注册"""

    def get(self, request):
        """处理GET请求,返回注册界面"""
        return HttpResponse('返回注册页面')

    def post(self, request):
        """处理POST请求,实现注册逻辑"""
        return HttpResponse('实现了注册逻辑')


# 定义一个为函数视图准备的装饰器
def my_decorate(func):
    print('装饰器调用前')
    def wrapper(request, *args, **kwargs):
        print('自定义装饰器被调用了')
        print('请求路径 %s' % request.path)
        return func(request, *args, **kwargs)
    return wrapper


class Demoview(View):

    """
    在类视图中使用为函数视图准备的装饰器时，不能直接添加装饰器，
    需要使用method_decorator将其转换为适用于类视图方法的装饰器。
    method_decorator的作用是为函数视图装饰器补充第一个self参数，以适配类视图方法。
    """
    # 为全部请求方法添加装饰器
    @method_decorator(my_decorate)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        print('get方法')
        return HttpResponse('ok')

    def post(self,resquest):
        print('post方法')
        return HttpResponse('ok')
