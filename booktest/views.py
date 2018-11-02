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


class IndexView(View):
    def get(self, request):
        context = {
            'city': '北京',
            'alist': [11, 22, 33, 44],
            'adict': {
                'name': 'laowang',
                'age': 18
            }
        }
        return render(request, 'index.html', context)
