"""
URL configuration for healthinsight project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from doctor import views as doc_views
from django.contrib.auth import views as auth_views
from patient import views as pat_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logindoc/',auth_views.LoginView.as_view(template_name='doctor/login.html'),name='doc-login'),
    path('registerdoc/',doc_views.register,name="doc-register"),
    path('doctorLogin/',doc_views.doctorlogin,name="d-login"),
    path('loginpat/',auth_views.LoginView.as_view(template_name='patient/login.html'),name='pat-login'),
    path('registerpat/',pat_views.register,name="pat-register"),
    path('patientLogin/',pat_views.patientlogin,name="p-login"),
    path('',include('minorproject.urls')),
]
