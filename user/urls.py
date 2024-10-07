from django.urls import path 
from . import views 
urlpatterns = [
    path("",views.home_view,name='home'),
    path("login",views.login_page,name='login'),
    path("logout",views.logout_page,name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path("signup",views.signup_view,name='signup'),
    path('verify_mfa/', views.verify_mfa, name='verify_mfa'),
    path('disable-2fa/', views.disable_2fa, name='disable_2fa'),

]