from rest_framework.response import Response
from rest_framework.views import APIView

from booktest.models import BookInfo
from booktest.serializers import BookInfoModelSerializer

"""
APIview的用法
接收的是REST framework的Request对象
返回REST framework的Response对象
"""
class BookListView(APIView):
    def get(self, request, ):
        queryset = BookInfo.query.all()
        s = BookInfoModelSerializer(queryset, many=True)
        return Response(s.data)

    def post(self, request):
        s = BookInfoModelSerializer(data=request.data)
        s.is_valid()
        print(s.validated_data)
        # s.create(s.validated_data)
        s.save()  # 模型序列化器的save()方法会自动调用create()方法
        return Response(s.validated_data)


class BookDetailView(APIView):
    def put(self, request, pk):
        book = BookInfo.query.get(pk=pk)
        # 指定partial=True,允许部分字段更新
        s = BookInfoModelSerializer(book, data=request.data, partial=True)
        s.is_valid(raise_exception=True)
        s.update(book, s.validated_data)
        return Response(s.validated_data)

