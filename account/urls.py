from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
   
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('dashboard',views.dashboard,name="dashboard"),
  
    path('logout',views.logout,name="logout"),
     path('profile',views.profile,name="profile"),
      path('profiledelete',views.profiledelete,name="profiledelete"),
]
