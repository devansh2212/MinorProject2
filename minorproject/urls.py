from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from doctor import views as doc_views

urlpatterns = [
    path('',views.home,name='minor-home'),
    path('logout/',auth_views.LogoutView.as_view(template_name='minorproject/logout.html'),name='logout'),
    path('profile/<str:user>/', views.profile, name='profile'),
    path('dashboard/<str:user>/', views.dashboard, name='dashboard'),
    path('dashboard/',doc_views.dashboard,name='dash')
]