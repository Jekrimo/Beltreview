from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/create$', views.createuser),
    url(r'^user/login$', views.loginuser),
    url(r'^user/(?P<id>\d+)$', views.showuser),
    url(r'^books$', views.show),
    url(r'^logout$', views.logout),
    url(r'^books/add$', views.addbook),
    url(r'^books/create$', views.createbook),
    url(r'^books/(?P<id>\d+)$', views.showbook),
    url(r'^create/review/(?P<id>\d+)$', views.createreview),
]
