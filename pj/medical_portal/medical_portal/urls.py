from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('main-menu/', views.main_menu_view, name='main_menu'),
    path('logout/', views.logout_view, name='logout'),
]