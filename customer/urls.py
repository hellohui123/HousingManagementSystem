#coding=utf-8
from django.conf.urls import url, include
from django.contrib import admin
import views
urlpatterns = {
    url(r'^$', views.main_view),
    url(r'^center.html$', views.center),
    url(r'^left.html$', views.left),
    url(r'^top.html$', views.top),
    url(r'^down.html$', views.down),
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

}
