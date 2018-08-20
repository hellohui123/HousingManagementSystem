from django.conf.urls import url

from employee import views

urlpatterns = {
    url(r'^center.html/$', views.center),
    url(r'^left.html/$', views.left),
    url(r'^top.html/$', views.top),
    url(r'^down.html/$', views.down),
    url(r'^login/$',views.Login.as_view()),
    url(r'^notice_list.html$',views.HandleNotice.as_view()),
    url(r'^delete_notice$',views.delete_notice),
    url(r'^add_notice/$',views.AddNotice.as_view()),
    url(r'^add_publisher/$',views.add_publisher),
    url(r'^dept_list.html$',views.Handle_dept.as_view()),
    url(r'^delete_dept$',views.delete_dept),
    url(r'^house_list.html$',views.HandleHouseInfo.as_view()),
    url(r'^delete_house_info$',views.delete_hosue_info),
    url(r'^update_house_info/$',views.UpdateHouseInfo.as_view()),
    url(r'^get_house_type/$',views.get_house_type),
    url(r'^receive_house_info/$',views.receive_house_info),
    url(r'^get_employee/$',views.get_employee),
    url(r'^add_house_info/$',views.Add_house_info.as_view()),
    url(r'^query_by_keys/$',views.Query_by_keys.as_view())
}