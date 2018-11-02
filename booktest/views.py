from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views import View


from .forms import BookForm


class BookView(View):
    def get(self, request):
        # 2.视图中使用表单类
        form = BookForm
        return render(request, 'book.html', {'form': form})

    def post(self, request):
        # 2.视图中使用表单类,并获取提交的数据
        form = BookForm(request.POST)
        if form.is_valid():  # 验证表单数据
            print(form.cleaned_data)  # 获取验证后的表单数据
            return HttpResponse("OK")
        return render(request, 'book.html', {'form': form})



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
