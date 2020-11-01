from django.urls import path,include
from .views import BaseView

urlpatterns = [
    path('', BaseView),
]
