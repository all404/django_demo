from django.conf.urls import url

# from classview import views
from classview.views import *

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    #  方法1 再URL配置中装饰
    url(r'^demo/$', my_decorate(Demoview.as_view()), name='register'),
]