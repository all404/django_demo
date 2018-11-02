from django.conf.urls import url

from booktest import views

urlpatterns = [
    url(r'^booktest/$', views.BookView.as_view(), name="booktest")
]