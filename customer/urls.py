#coding=utf-8
from django.conf.urls import url, include
from django.contrib import admin
import views
urlpatterns = {
    url(r'^$', views.index_view),
    url(r'^center.html', views.center),
    url(r'^left.html', views.left),
    url(r'^top.html', views.top),
    url(r'^down.html', views.down),

}
