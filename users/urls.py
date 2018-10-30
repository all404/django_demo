from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^say/$', views.say),
]
