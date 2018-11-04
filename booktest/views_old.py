import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from booktest.forms import BookForm
from booktest.models import BookInfo, HeroInfo

from datetime import datetime

from booktest.serializers import BookInfoSerializer, HeroInfoSerializer


# 演示序列化过程
def serializer(request):
    # 查询出模型对象
    # book = BookInfo.query.get(pk=1)

    booklist = BookInfo.query.all()

    # 将模型对象交给序列化器
    s = BookInfoSerializer(booklist, many=True)

    # hero = HeroInfo.query.get(pk=1)
    #
    # s = HeroInfoSerializer(hero)

    # 从序列化器的data属性中, 就能够获取挑选完成字段的数据
    print(s.data)
    # 需要将数据变成json字符串返回给前端. 用到了DRF里面的Response, 后面会讲到
    return HttpResponse("序列化成功! %s" % s.data)


# 演示反序列化过程
def deserializer(request):
    # 模拟前端提交的数据
    # data = {"id":1, "btitle": "西游记之Django开发", "bpub_date": "2000-01-01", "is_delete": 1, "bread": 100, "bcomment": 10}
    # data = {"hname": "猪八戒", "hbook": 100}
    data = {"btitle":"水浒传之Django开发5", "bpub_date": "2000-01-01"}

    # 查询数据库, 得到一个bookInfo模型对象, 用于进行更新
    book = BookInfo.query.get(pk=5)

    # s = BookInfoSerializer(book, data=data)
    s = BookInfoSerializer(data=data)
    # s = HeroInfoSerializer(data=data)

    # 判断前端数据是否合法, True表示合法
    print(s.is_valid(raise_exception=True))
    # 可以输出错误信息
    print(s.errors)
    # 可以提取处校验结束之后的干净数据
    print(s.validated_data)

    s.save()

    return HttpResponse("反序列化结束! %s" % s.validated_data)


class IndexView(View):
    def get(self, request):
        # # 1.获取模板
        # template = loader.get_template('index.html')
        #
        # # 2.渲染模板
        # return HttpResponse(template.render({"city":"北京"}))
        context = {
            "city": "西安",
            "alist": ["a", "b", "c", "d"],
            # "alist": [],
            "adict": {
                "name": "张三",
                "age": 18
            }
        }

        return render(request, "index.html", context)


class BookView(View):
    def get(self, request):
        form = BookForm()

        return render(request, "book.html", {"form": form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():  # 判断数据是否合法
            # 获取提交的数据
            print(form.cleaned_data)
            return HttpResponse("OK")

        return render(request, "book.html", {"form": form})


class BooksAPIView(View):
    # 获取所有图书数据
    def get(self, request):
        queryset = BookInfo.query.all()

        book_list = []
        for book in queryset:
            book_list.append({
                "id": book.id,
                "btitle": book.btitle,
                "bpub_date": book.bpub_date.strftime("%Y-%m-%d"),
                "bread": book.bread,
                "bcomment": book.bcomment,
                "image": book.image.url if book.image else ''
            })

        # 如果要传列表, 必须指定safe=False, 详见源码
        return JsonResponse(book_list, safe=False)

    # 新增图书
    def post(self, request):
        json_bytes = request.body
        json_str = json_bytes.decode()
        json_dict = json.loads(json_str)

        book = BookInfo.query.create(
            btitle=json_dict.get("btitle"),
            bpub_date=datetime.strptime(json_dict.get("bpub_date"), "%Y-%m-%d").date()
        )

        return JsonResponse({
            "id": book.id,
            "btitle": book.btitle,
            "bpub_date": book.bpub_date.strftime("%Y-%m-%d"),
            "bread": book.bread,
            "bcomment": book.bcomment,
            "image": book.image.url if book.image else ''
        }, status=201)


class BookAPIView(View):
    # 获取单个图书信息
    def get(self, request, pk):
        try:
            book = BookInfo.query.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        return JsonResponse({
            "id": book.id,
            "btitle": book.btitle,
            "bpub_date": book.bpub_date.strftime("%Y-%m-%d"),
            "bread": book.bread,
            "bcomment": book.bcomment,
            "image": book.image.url if book.image else ''
        })

    # 修改单个图书
    def put(self, request, pk):
        try:
            book = BookInfo.query.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        json_bytes = request.body
        json_str = json_bytes.decode()
        json_dict = json.loads(json_str)

        book.btitle = json_dict.get("btitle")
        book.bpub_date = datetime.strptime(json_dict.get("bpub_date"), "%Y-%m-%d").date()
        book.save()

        return JsonResponse({
            "id": book.id,
            "btitle": book.btitle,
            "bpub_date": book.bpub_date.strftime("%Y-%m-%d"),
            "bread": book.bread,
            "bcomment": book.bcomment,
            "image": book.image.url if book.image else ''
        })

    # 删除单个图书
    def delete(self, request, pk):
        try:
            book = BookInfo.query.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        book.delete()

        return HttpResponse(status=204)
