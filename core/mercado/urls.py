from django.urls import path,include
from .views import BaseView

urlpatterns = [
    path('', BaseView),
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardView,name="dashboard")
    path('login/',),
    path('register/',views.registerView,name="register_url"),
    path('logout/',),

]
