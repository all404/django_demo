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


# 定义两个为函数视图准备的装饰器
def my_decorate(func):
    print('装饰器调用前')
    def wrapper(request, *args, **kwargs):
        print('before request 装饰器被调用了')
        result = func(request, *args, **kwargs)
        print('after request 装饰器被调用了')
        return result
    return wrapper

def my_decorate222(func):
    print('装饰器222调用前')
    def wrapper(request, *args, **kwargs):
        print('before request 装饰器222被调用了')
        result = func(request, *args, **kwargs)
        print('after request 装饰器222被调用了')
        return result
    return wrapper


# 1.定义的扩展类继承object,重写as_view()方法,添加装饰器my_decorate
class MyDecoratorMixin(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        view = my_decorate(view)
        return view
# 2.定义扩展类都继承object,重写as_view()方法,添加装饰器my_decorate2
class MyDecoratorMixin2(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        view = my_decorate222(view)
        return view


# 3.让类视图继承需要的扩展类,并且继承View类
class Demoview(MyDecoratorMixin, MyDecoratorMixin2, View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        print('get方法')
        return HttpResponse('ok')

    def post(self,resquest):
        print('post方法')
        return HttpResponse('ok')


# # 1.创建一个类集成View,重写as_view()方法添加装饰
# class BaseView(View):
#     def as_view(cls, **initkwargs):
#         view = super().as_view(**initkwargs)
#         view = my_decorate(view)
#         return view
#
# # 2.让视图类继承上面的类,这样也会为视图函数添加了装饰器
# class Demoview(BaseView):
#
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def get(self, request):
#         print('get方法')
#         return HttpResponse('ok')
#
#     def post(self,resquest):
#         print('post方法')
#         return HttpResponse('ok')



# # 使用name参数指明被装饰的方法
# # @method_decorator(my_decorate, name='dispatch')
# @method_decorator(my_decorate, name='get')
# class Demoview(View):
#
#     """
#     在类视图中使用为函数视图准备的装饰器时，不能直接添加装饰器，
#     需要使用method_decorator将其转换为适用于类视图方法的装饰器。
#     method_decorator的作用是为函数视图装饰器补充第一个self参数，以适配类视图方法。
#     """
#     # 为全部请求方法添加装饰器
#     # @method_decorator(my_decorate)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     # 为特定方法添加装饰器
#     # @method_decorator(my_decorate)
#     def get(self, request):
#         print('get方法')
#         return HttpResponse('ok')
#
#     def post(self,resquest):
#         print('post方法')
#         return HttpResponse('ok')
