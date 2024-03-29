"""apollo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from nplmis import views
from django.conf.urls import include, url

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.init_web),
    url(r'^logout/', views.init_web),
    url(r'^create_user/', views.create_user),
    url(r'^get_all_user_info/', views.get_all_user_info),
    url(r'^user_login/', views.user_login),
    url(r'^get_user_info_by_id/', views.get_user_info_by_id),
    url(r'^modify_user/', views.modify_user),
    url(r'^remove_user/', views.remove_user),
   
    url(r'^manage_user', views.manage_user),
    url(r'^manage_payment', views.manage_payment),
    url(r'^manage_student', views.manage_student),
    url(r'^manage_p_class', views.manage_p_class),
    url(r'^manage_class', views.manage_class),
    url(r'^manage_report', views.manage_report),
    url(r'^settings', views.manage_settings),
    url(r'^audio_upload', views.audio_upload),
    url(r'^upload', views.upload),
    

]


handler404 = views.page_not_found