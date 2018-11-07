"""mysites URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from cmdb import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'test/', views.test),
    url(r'teeth/', views.teeth),
    url(r'home/', views.home),
    url(r'iframe/', views.iframe),
    url(r'contact/', views.contact),
    url(r'system/', views.system),
    url(r'index', views.index),
    url(r'second', views.second),
    url(r'system2', views.system2),
    url(r'^get_desc$', views.get_desc, name='get_disc'),
    url(r'^get_flag$', views.get_flag, name='get_flag'),
    url(r'^get_desc2$', views.get_desc2, name='get_disc2'),
    url(r'^get_table$', views.get_table, name='get_table'),
    url(r'^get_plan$', views.get_plan, name='get_plan'),
    url(r'^get_picture$', views.get_picture, name='get_picture'),
    url(r'^get_teeth$', views.get_teeth, name='get_teeth'),
]
