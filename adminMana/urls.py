#coding=utf-8
from django.conf.urls import url
import views

urlpatterns=[
    url(r'^employee_add',views.employee_views),#员工添加页面
    url(r'^deal_employee_add',views.deal_employee_add),#处理员工添加功能
    url(r'^department_add',views.department_views),#添加部门页面
    url(r'^deal_department_add',views.deal_department_add),#处理添加部门功能
    url(r'^role_add',views.role_add_views),#添加角色功能页面
    url(r'^deal_role_add',views.deal_role_add),#处理添加角色功能
    url(r'^deal_exist_role',views.deal_already_exist)#处理已有角色功能
]