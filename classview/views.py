from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class RegisterView(View):
    """类视图: 处理注册"""

    def get(self, request):
        """处理GET请求,返回注册界面"""
        return HttpResponse('返回注册页面')

    def post(self, request):
        """处理POST请求,实现注册逻辑"""
        return HttpResponse('实现了注册逻辑')
