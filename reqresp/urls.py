from django.conf.urls import url

from reqresp import views

urlpatterns = [
    # 定义路由URL时,未命名参数按定义顺序传递给视图
    # url(r'reqresp/([a-z]+)/(\d{4})/', views.weather, name='reqresp'),
    # 命名参数按名字传递
    url(r'reqresp/(?P<city>[a-z]+)/(?P<year>\d{4})/', views.weather, name='reqresp'),
    url(r'reqresp/getbody/$', views.get_body),
    url(r'reqresp/getjson/$', views.get_body_json),
    url(r'reqresp/getheaders/$', views.get_headers),
    url(r'reqresp/demoview/$', views.demo_view),
]
