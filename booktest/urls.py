from django.conf.urls import url

from booktest import views
from booktest import views_new
from booktest import views_old

urlpatterns = [
    # url(r'^booktest/$', views.BookView.as_view(), name="booktest"),
    # url(r'^index/$', views.IndexView.as_view()),
    # url(r'^books/$', views.BooksAPIView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookAPIView.as_view()),
    # url(r'^ser/$', views.serialize),
    # url(r'^deser/$', views.deserialize),
    # url(r'^books/$', views.BookListView.as_view()),
    # url(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view()),
    # url(r'^index/$', views_old.IndexView.as_view()),
    # url(r'^book/$', views_old.BooksAPIView.as_view()),
    # url(r'^book/(?P<pk>\d+)$', views_old.BookAPIView.as_view()),
    # url(r'^heroes/$', views.HeroListView.as_view()),
    # url(r'^heroes/(?P<pk>\d+)$', views.HeroDetailView.as_view()),
    url(r'^books/$', views_new.BookListView.as_view()),
    url(r'^books/(?P<pk>\d+)$', views_new.BookDetailView.as_view()),
]
