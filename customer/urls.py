#coding=utf-8
from django.conf.urls import url, include
from django.contrib import admin
import views
urlpatterns = {
    url(r'^$', views.index_view),
    url(r'^center.html', views.center),
    url(r'^left.html', views.left),
    url(r'^customer_type1',views.customerType1),#进入客户类型页面
    url(r'^customer_add',views.customer_add),#进入添加页面
    url(r'^deal_customer_add',views.deal_customer_add),#处理添加功能
    url(r'^deal_customer_query',views.deal_customer_query),#处理查询功能
    url(r'^deal_customer_page',views.deal_customer_page),#处理分页功能
    url(r'^deleteData',views.deal_customer_delete),#处理删除功能
    url(r'^top.html', views.top),
    url(r'^down.html', views.down),

}
