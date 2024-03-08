from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.Login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.Logout,name='logout'),
    
]


