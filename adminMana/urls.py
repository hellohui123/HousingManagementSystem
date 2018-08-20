from django.conf.urls import url

from adminMana import views

urlpatterns = {
    url(r'^center.html', views.center),
    url(r'^left.html', views.left),
    url(r'^top.html', views.top),
    url(r'^down.html', views.down),

}