#coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^house_type',views.house_type_view),#跳转到房屋类型页面
    url(r'^house_add',views.house_add),#跳转到房屋添加页面
    url(r'^deal_house_add',views.deal_house_add),#处理房屋类型添加功能
    url(r'^deal_house_type_query',views.deal_house_type_query),#处理房屋类型查询功能
    url(r'^deal_house_delete',views.deal_house_delete),#处理房屋删除功能
]