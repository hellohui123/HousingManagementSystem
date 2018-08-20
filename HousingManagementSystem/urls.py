"""HousingManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^customer/',include('customer.urls')),
    url(r'^employee/',include('employee.urls')),
    url(r'^adminMana/', include('adminMana.urls')),

=======
    url(r'^main/',include('customer.urls')),
    url(r'^employee/',include('employee.urls'))
>>>>>>> 5eb9938e74366b08ad26ef23b0627190108e9648
]
