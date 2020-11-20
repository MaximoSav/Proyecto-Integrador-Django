from django.urls import path,include
from . import views
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', BaseView, name="base_url"),
    path('accounts/login/', LoginView.as_view(), name="login_url"),
    path('accounts/register/', views.registerView, name="register_url"),
    path('accounts/logout/', views.logoutView, name="logout_url"),
]
