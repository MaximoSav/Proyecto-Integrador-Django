from django.urls import path,include
from . import views
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', BaseView),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('accounts/login/',LoginView.as_view(),name="login_url"),
    path('accounts/register/',views.registerView,name="register_url"),

]
