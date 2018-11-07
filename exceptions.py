from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework import status
from django.db import DatabaseError


def exception_handler(exc, context):

    # 如果drf能够处理异常, 那么就会得到一个response对象, 响应给前端
    # 如果drf无法处理改异常, 就会返回None
    response = drf_exception_handler(exc, context)

    if response is None:
        view = context['view']
        if isinstance(exc, DatabaseError):
            print('[%s]: %s' % (view, exc))
            response = Response({'detail': '服务器内部错误'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
        else:
            print('[%s]: %s' % (view, exc))
            response = Response({'detail': '服务器内部错误'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
