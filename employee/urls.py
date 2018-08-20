#coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^empl_list.html',views.get_em_list),
    url(r'^delUserInfo/',views.deleteUserInfo),
    url(r'^emp_edit.html',views.get_emp_edit),
    url(r'^userUpdateServlet/',views.userUpdateServlet),
    url(r'emp_detail.html',views.emp_detail)
]