#coding=utf-8
from django.conf.urls import url, include
from django.contrib import admin

from customer import views

urlpatterns = {
    url(r'^$', views.index_view),
    url(r'^center.html$', views.center),
    url(r'^left.html$', views.left),
    url(r'^top.html$', views.top),
    url(r'^down.html$', views.down),
    url(r'^customer_source_list.html/$',views.customer_list),
    url(r'^query_customer_source/$',views.query_customer_source),
    url(r'^delete_one$',views.delete_one),
    url(r'^customer_source_add.html$',views.CustomerSourceAdd.as_view())


}
