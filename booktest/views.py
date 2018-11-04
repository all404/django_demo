# import json
# from datetime import datetime
#
# from django.http import HttpResponse
# from django.http import JsonResponse
# from django.shortcuts import render
#
# # Create your views here.
# from django.template import loader
# from django.views import View
#
# from booktest.models import BookInfo
# from .forms import BookForm
#
#
# # 使用序列化器
# from .serializers import BookInfoSerializer
# # 执行序列化的视图
# def serialize(request):
#     # 从数据库中查询出模型对象
#     book = BookInfo.query.get(id=1)
#     # 初始化序列化器,需要把模型对象传给序列化器
#     serializer = BookInfoSerializer(book)
#
#     # 若查询出来的是查询结果集,需要指定many参数
#     books = BookInfo.query.all()
#     serializer2 = BookInfoSerializer(books, many=True)
#
#     # 序列化成功的结果
#     print(serializer.data)
#     print(type(serializer.data))
#     print(serializer2.data)
#     return HttpResponse('序列化成功! %s' % serializer.data)
#
# # 执行反序列化的视图
# def deserialize(request):
#     # 模拟客户端提交的数据
#     data = {'btitle': '倚天屠龙记', 'bpub_date': '1999-10-10'}
#     # 初始化序列化器,需要把数据传给参数data
#     serializer = BookInfoSerializer(data=data)
#     # 获取校验的结果
#     print(serializer.is_valid())
#     # 校验失败的错误信息
#     print(serializer.errors)
#     # 校验成功的干净的数据(返回的是有序字典OrderedDict)
#     print(serializer.validated_data)
#     return HttpResponse('反序列化结束!!! %s' % serializer.validated_data)
#
#
# class BookView(View):
#     def get(self, request):
#         # 2.视图中使用表单类
#         form = BookForm
#         return render(request, 'book.html', {'form': form})
#
#     def post(self, request):
#         # 2.视图中使用表单类,并获取提交的数据
#         form = BookForm(request.POST)
#         if form.is_valid():  # 验证表单数据
#             print(form.cleaned_data)  # 获取验证后的表单数据
#             return HttpResponse("OK")
#         return render(request, 'book.html', {'form': form})
#
#
# class IndexView(View):
#     def get(self, request):
#         context = {
#             'city': '北京',
#             'alist': [11, 22, 33, 44],
#             'adict': {
#                 'name': 'laowang',
#                 'age': 18
#             }
#         }
#         return render(request, 'index.html', context)
#
#
# """使用Django开发REST接口(使用Postmain测试接口)"""
# class BooksAPIView(View):
#     """查询所有图书,增加图书"""
#     def get(self, request):
#         """
#          获取所有图书
#          路由 GET /books/
#         """
#         queryset = BookInfo.query.all()
#         book_list = []
#         for book in queryset:
#             b = {
#                 'id': book.id,
#                 'btitle': book.btitle,
#                 'bpub_date': book.bpub_date,
#                 'bread': book.bread,
#                 'bcomment': book.bcomment,
#                 'image': book.image.url if book.image else ''
#             }
#             book_list.append(b)
#         # 如果要传列表, 必须指定safe=False, 详见源码
#         return JsonResponse(book_list, safe=False)
#
#     def post(self,request):
#         """
#         增加图书
#         路由 POST /books/
#         """
#         json_bytes = request.body
#         json_str = json_bytes.decode()
#         json_dict = json.loads(json_str)
#         # 作为测试,详细校验的代码省略
#         book = BookInfo.query.create(
#             btitle=json_dict.get('btitle'),
#             bpub_date=datetime.strptime(json_dict.get('bpub_date'), '%Y-%m-%d').date()
#         )
#         return JsonResponse(
#             {
#                 'id': book.id,
#                 'btitle': book.btitle,
#                 'bpub_date': book.bpub_date,
#                 'bread': book.bread,
#                 'bcomment': book.bcomment,
#                 'image': book.image if book.image else ''
#             },
#             status=201
#         )
#
# class BookAPIView(View):
#     """获取,修改,删除图书单个图书"""
#     def get(self, request, pk):
#         """
#         获取单个图书信息
#          路由 GET /book/pk
#         """
#         try:
#             book = BookInfo.query.get(pk=pk)
#         except BookInfo.DoesNotExist:
#             return HttpResponse(status=404)
#         return JsonResponse({
#             'id': book.id,
#             'btitle': book.btitle,
#             'bpub_date': book.bpub_date,
#             'bread': book.bread,
#             'bcomment': book.bcomment,
#             'image': book.image if book.image else ''
#         })
#
#     def put(self, request, pk):
#         """
#         修改单个图书信息
#         路由 PUT /book/pk
#         """
#         try:
#             book = BookInfo.query.get(pk=pk)
#         except BookInfo.DoesNotExist:
#             return HttpResponse(status=404)
#
#         json_bytes = request.body
#         json_str = json_bytes.decode()
#         json_dict = json.loads(json_str)
#         # 参数校验代码省略
#         book.btitle = json_dict.get('btitle')
#         book.bpub_date = datetime.strptime(json_dict.get('bpub_date'), '%Y-%m-%d').date()
#         book.save()
#
#         return JsonResponse({
#             'btitle': book.btitle,
#             'bpub_date': book.bpub_date,
#             'bread': book.bread,
#             'bcomment': book.bcomment,
#             'image': book.image if book.image else ''
#         })
#
#     def delete(self, request, pk):
#         """
#         删除单个图书
#          路由 DELETE /book/pk
#         """
#         try:
#             book = BookInfo.query.get(pk=pk)
#         except BookInfo.DoesNotExist:
#             return HttpResponse(status=404)
#         book.delete()
#         return HttpResponse(status=204)


from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from booktest.models import BookInfo
from booktest.serializers import BookInfoModelSerializer


# class BookListView(APIView):
#
#     def get(self,request):
#         queryset = BookInfo.query.all()
#         serializer = BookInfoModelSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = BookInfoModelSerializer(data=request.data)
#
#     def put(self, request):
#         book = BookInfo.query.get(pk=1)
#         serializer = BookInfoModelSerializer(book, data=request.data)


class BookListView(GenericAPIView):

    # 指定查询结果集
    queryset = BookInfo.query.all()
    # 指定序列化器类
    serializer_class = BookInfoModelSerializer

    def get(self, request):
        # 获取查询结果集
        books = self.get_queryset()
        # 获取序列化器对象
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)


class BookDetailView(GenericAPIView):
    # 指定查询结果集
    # queryset = BookInfo.query.all()
    # 指定序列化器类
    # serializer_class = BookInfoModelSerializer
    lookup_field = 'pk'  # 查询单一数据库对象时使用的字段名，默认为'pk'
    lookup_url_kwarg = 'pk'  # 查询单一数据时URL中的参数关键字名称，默认'pk'

    # 可以重写get_queryset()方法返回查询结果集
    def get_queryset(self):
        return BookInfo.query.all()

    # 重写get_serializer_class()方法指定序列化器
    def get_serializer_class(self):
        return BookInfoModelSerializer

    def get(self, request, pk):
        book = self.get_object()  # 获取单个数据
        serializer = self.get_serializer(book)
        return Response(serializer.data)
