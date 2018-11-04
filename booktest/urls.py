from django.conf.urls import url

from booktest import views

urlpatterns = [
    # url(r'^booktest/$', views.BookView.as_view(), name="booktest"),
    # url(r'^index/$', views.IndexView.as_view()),
    # url(r'^books/$', views.BooksAPIView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookAPIView.as_view()),
    # url(r'^ser/$', views.serialize),
    # url(r'^deser/$', views.deserialize),
    url(r'^books/$', views.BookListView.as_view()),
    url(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view()),
]