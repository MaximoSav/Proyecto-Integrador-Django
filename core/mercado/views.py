from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def BaseView(request):
    return render(request, 'mercado/base.html', {'name': request.user,})
