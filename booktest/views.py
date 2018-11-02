from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views import View


class BookView(View):

    def get(self, request):

        """渲染模板普通写法"""
        # # 1.加载模板
        # template = loader.get_template('index.html')
        # # 2.渲染模板
        # return HttpResponse(template.render({"city": "北京"}))

        """渲染模板简写"""
        return render(request, 'index.html', {"city": "西安"})
