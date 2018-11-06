from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from booktest.models import BookInfo
from booktest.serializers import BookInfoModelSerializer

"""
APIview的用法
接收的是REST framework的Request对象
返回REST framework的Response对象
"""
# class BookListView(APIView):
#     def get(self, request, ):
#         queryset = BookInfo.query.all()
#         s = BookInfoModelSerializer(queryset, many=True)
#         return Response(s.data)
#
#     def post(self, request):
#         s = BookInfoModelSerializer(data=request.data)
#         s.is_valid()
#         print(s.validated_data)
#         # s.create(s.validated_data)
#         s.save()  # 模型序列化器的save()方法会自动调用create()方法
#         return Response(s.validated_data)
#
#
# class BookDetailView(APIView):
#     def put(self, request, pk):
#         book = BookInfo.query.get(pk=pk)
#         # 指定partial=True,允许部分字段更新
#         s = BookInfoModelSerializer(book, data=request.data, partial=True)
#         s.is_valid(raise_exception=True)
#         s.update(book, s.validated_data)
#         return Response(s.validated_data)


"""
GenericAPIView的用法
继承自APIVIew，增加了对于列表视图和详情视图可能用到的通用支持方法。通常使用时，可搭配一个或多个Mixin扩展类。
支持定义的属性举例：
    queryset 视图查询结果集
    serializer_class 使用的序列化器
    pagination_class 使用的分页控制类
    filter_backends 使用的过滤控制后端
    lookup_field 从数据库查询单一数据使用的参数名,默认'pk'
    lookup_url_kwarg 在url中的参数名称,默认=look_field
提供的方法:
    get_queryset(self)
    get_serializer_class(self)
    get_serializer(self, args, *kwargs)
    get_object(self)
"""
# class BookListView(GenericAPIView):
#     queryset = BookInfo.query.all()
#     serializer_class = BookInfoModelSerializer
#
#     def get(self, request):
#         books = self.get_queryset()
#         s = self.get_serializer(books, many=True)
#         return Response(s.data)
#
#     def post(self, request):
#         s = self.get_serializer(data=request.data)
#         s.is_valid()
#         s.save()
#         return Response(s.validated_data)
#
# class BookDetailView(GenericAPIView):
#     queryset = BookInfo.query.all()
#     serializer_class = BookInfoModelSerializer
#     lookup_field = 'id'
#     lookup_url_kwarg = 'pk'
#     def put(self, request, pk):
#         book = self.get_object()
#         s = self.get_serializer(book, data=request.data, partial=True)
#         s.is_valid(raise_exception=True)
#         s.save()  # save()方法会根据是创建还是更新,自动调用create()或者update()
#         return Response(s.validated_data)


"""
扩展类用法介绍
五个动作对应五个扩展类
1）ListModelMixin --list(request, *args, **kwargs)方法快速实现列表视图，返回200状态码。
2）CreateModelMixin --create(request, *args, **kwargs)方法快速实现创建资源的视图，成功返回201状态码。
3）RetrieveModelMixin --retrieve(request, *args, **kwargs)方法，可以快速实现返回一个存在的数据对象。
4）UpdateModelMixin --update(request, *args, **kwargs)方法，可以快速实现更新一个存在的数据对象。
                    --partial_update(request, *args, **kwargs)方法，可以实现局部更新。
5）DestroyModelMixin --提供destroy(request, *args, **kwargs)方法，可以快速实现删除一个存在的数据对象。


"""
# class BookListView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = BookInfo.query.all()
#     serializer_class = BookInfoModelSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class BookDetailView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
#     queryset = BookInfo.query.all()
#     serializer_class = BookInfoModelSerializer
#
#     def get(self, request, pk):
#         return self.retrieve(request, pk)
#
#     def put(self, request, pk):
#         return self.update(request, pk)
#
#     def delete(self, request, pk):
#         return self.destroy(request, pk)


"""
几个可用子类视图的使用
1）ListAPIView --提供 get 方法,继承自：GenericAPIView、ListModelMixin
2）CreateAPIView --提供 post 方法,继承自： GenericAPIView、CreateModelMixin
3)ListCreateAPIView --提供 get post 方法,继承自：GenericAPIView、ListModelMixin、CreateModelMixin
4）RetireveAPIView --提供 get 方法,继承自: GenericAPIView、RetrieveModelMixin
5）DestoryAPIView --提供 delete 方法,继承自：GenericAPIView、DestoryModelMixin
6）UpdateAPIView --提供 put 和 patch 方法,继承自：GenericAPIView、UpdateModelMixin
7）RetrieveUpdateAPIView --提供 get、put、patch方法,继承自： GenericAPIView、RetrieveModelMixin、UpdateModelMixin
8)RetrieveDestroyAPIView --提供 get delete方法,继承自： GenericAPIView、RetrieveModelMixin、DestroyModelMixin
9）RetrieveUpdateDestoryAPIView
    提供 get、put、patch、delete方法,继承自：GenericAPIView、RetrieveModelMixin、UpdateModelMixin、DestroyModelMixin
"""
# class BookListView(ListCreateAPIView):
#     queryset = BookInfo.query.all()
#     serializer_class = BookInfoModelSerializer
#
# class BookDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = BookInfo.query.all()
#     serializer_class = BookInfoModelSerializer


"""
视图集用法
视图集类不再实现get()、post()等方法，而是实现动作 action 如 list() 、create() 等。
1）ViewSet --继承自APIView，作用也与APIView基本类似没有提供任何动作action方法，需要我们自己实现action方法。
2）GenericViewSet --继承自GenericAPIView，作用也与GenericAPIVIew类似
3）ModelViewSet --继承自GenericAPIVIew,
            同时包括了ListModelMixin、RetrieveModelMixin、CreateModelMixin、UpdateModelMixin、DestroyModelMixin。
            默认5个动作, list, create, retrieve, update, destroy
4）ReadOnlyModelViewSet --继承自GenericAPIVIew，同时包括了ListModelMixin、RetrieveModelMixin。
"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
class BookAPIView(ModelViewSet):
    queryset = BookInfo.query.all()
    serializer_class = BookInfoModelSerializer
    # url的配置方式, as_view({'get': 'list'})传递字典, 描述请求方法和动作的对应关系

    # 可以自定义附加action动作
    @action(methods=['get'], detail=False)
    def latest(self, request):
        book = BookInfo.query.latest('id')
        s = self.get_serializer(book)
        return Response(s.data)


"""
路由Routers的用法
对于视图集ViewSet，还可以使用Routers来帮助我们快速实现路由列表信息。
SimpleRouter
DefaultRouter
"""
