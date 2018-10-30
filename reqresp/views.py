from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.

def weather(request, year, city):

    # 使用正则表达式提取参数的方法从URL中获取请求参数,Django会将提取的参数直接传递到视图的传入参数中。
    print('city:', city)
    print('year:', year)

    # 获取请求路径中的查询字符串参数（形如?a=v1&b=v2）,通过request.GET属性获取,返回QueryDict对象.
    # 再调用get()方法获取数据,getlist()获取多个同名参数的值,返回列表
    a = request.GET.get('a')
    b = request.GET.get('b')
    a_list = request.GET.getlist('a')
    print('a:', a)
    print('b:', b)
    print('a_list:', a_list)

    return HttpResponse('OK')
    # 查询字符串不区分请求方式，即假使客户端进行POST方式的请求，依然可以通过request.GET获取请求中的查询字符串数据。


def get_body(request):
    """获取请求体视图
    请求体数据格式，可以是表单类型字符串，可以是JSON字符串，可以是XML字符串，应区别对待。
    可以发送请求体数据的请求方式有POST、PUT、PATCH、DELETE。
    测试时可以关闭CSRF防护
    """
    # 表单类型请求体数据, 通过request.POST获取,返回QueryDict对象
    a = request.POST.get('a')  # get()若同一个参数名有多个值,获取最后一个
    b = request.POST.get('b')
    a_list = request.POST.getlist('a')
    print('a:', a)
    print('b:', b)
    print('a_list:', a_list)
    return HttpResponse('get body ok')
    # 只要请求体的数据是表单类型，无论是哪种请求方式（POST、PUT、PATCH、DELETE）,都是使用request.POST来获取请求体的表单数据。

import json


def get_body_json(request):
    """
    非表单类型的请求体数据，Django无法自动解析，可以通过request.body属性获取最原始的请求体数据
    自己按照请求体格式（JSON、XML等）进行解析
    request.body返回bytes类型。
    """
    # 例如获json类型数据{"a": 1, "b": 2}
    json_str = request.body
    json_str = json_str.decode()  # 解码成字符串, python3.6无需执行此步
    req_data = json.loads(json_str)
    print(req_data['a'])
    print(req_data['b'])

    return HttpResponse('get jsnon ok')


def get_headers(request):
    """
    request.META属性获取请求头headers中的数据, request.META为字典类型。
    """
    # 获取请求头Content-Type
    print(request.META['CONTENT_TYPE'])
    return HttpResponse('get headers ok')


def demo_view(request):
    """
    可以使用django.http.HttpResponse来构造响应对象。
    Response(content=响应体, content_type=响应体数据类型, status=状态码)
    也可通过HttpResponse对象属性来设置响应体、响应体数据类型、状态码：
    content：表示返回的内容。
    status_code：返回的HTTP响应状态码。
    content_type：指定返回数据的的MIME类型。
    """
    # return HttpResponse('name: zhangsan', status=222)
    #
    # response = HttpResponse()
    # response['Name'] = 'Zhangsan'  # 自定义响应头'Name', 值为'Zhangsan'
    # response.status_code = 400
    # return response

    """
    若要返回json数据，可以使用JsonResponse来构造响应对象，作用：
    帮助我们将数据转换为json字符串
    设置响应头Content-Type为application/json
    """
    # return JsonResponse({'city': 'beijing', 'weather': 'sunny'})

    """重定向"""
    return redirect('/static/index.html')
