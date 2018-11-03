import json
from datetime import datetime

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views import View

from booktest.models import BookInfo
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


"""使用Django开发REST接口(使用Postmain测试接口)"""
class BooksAPIView(View):
    """查询所有图书,增加图书"""
    def get(self, request):
        """
         获取所有图书
         路由 GET /books/
        """
        queryset = BookInfo.query.all()
        book_list = []
        for book in queryset:
            b = {
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'image': book.image.url if book.image else ''
            }
            book_list.append(b)
        # 如果要传列表, 必须指定safe=False, 详见源码
        return JsonResponse(book_list, safe=False)

    def post(self,request):
        """
        增加图书
        路由 POST /books/
        """
        json_bytes = request.body
        json_str = json_bytes.decode()
        json_dict = json.loads(json_str)
        # 作为测试,详细校验的代码省略
        book = BookInfo.query.create(
            btitle=json_dict.get('btitle'),
            bpub_date=datetime.strptime(json_dict.get('bpub_date'), '%Y-%m-%d').date()
        )
        return JsonResponse(
            {
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'image': book.image if book.image else ''
            },
            status=201
        )

class BookAPIView(View):
    """获取,修改,删除图书单个图书"""
    def get(self, request, pk):
        """
        获取单个图书信息
         路由 GET /book/pk
        """
        try:
            book = BookInfo.query.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)
        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image if book.image else ''
        })

    def put(self, request, pk):
        """
        修改单个图书信息
        路由 PUT /book/pk
        """
        try:
            book = BookInfo.query.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        json_bytes = request.body
        json_str = json_bytes.decode()
        json_dict = json.loads(json_str)
        # 参数校验代码省略
        book.btitle = json_dict.get('btitle')
        book.bpub_date = datetime.strptime(json_dict.get('bpub_date'), '%Y-%m-%d').date()
        book.save()

        return JsonResponse({
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image if book.image else ''
        })

    def delete(self, request, pk):
        """
        删除单个图书
         路由 DELETE /book/pk
        """
        try:
            book = BookInfo.query.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)
        book.delete()
        return HttpResponse(status=204)