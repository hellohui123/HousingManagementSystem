#coding=utf-8
from django.conf.urls import url, include
from django.contrib import admin

from customer import views

urlpatterns = [
    url(r'^$', views.index_view),
    url(r'^center.html', views.center),
    url(r'^left.html', views.left),
    url(r'^top.html', views.top),
    url(r'^down.html', views.down),
    url(r'^customer_distribute_list.html/$',views.get_page),
    url(r'^customer_allot/',views.customer_allot),#分配所选客户
    url(r'^userAllot/',views.userAllot),
    url(r'^customer_source_list.html/$',views.customer_list),
    url(r'^query_customer_source/$',views.query_customer_source),
    url(r'^delete_one$',views.delete_one),
    url(r'^customer_source_add.html$',views.CustomerSourceAdd.as_view()),
    url(r'^get_careObj/$', views.get_careObj),
    url(r'^get_linkObj/$', views.get_linkObj),
    url(r'^get_noticeObj', views.get_noticeObj),
    url(r'^get_birthObj', views.get_birthObj),
    url(r'^customer_list1.html', views.get__customerList1),
    url(r'^customer_edit.html', views.get_customer_edit),
    url(r'^customer_detail.html', views.get_customer_detail),
    url(r'^customerUpdateServlet/', views.customerUpdateServlet),
    url(r'^deleteCusInfo/',views.deleteCusInfo),
    url(r'^createCustomer/',views.createCustomer),
    url(r'^skip5seconds',views.skip5seconds)


]
