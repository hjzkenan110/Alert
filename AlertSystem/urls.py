"""AlertSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from alert import views as alert

import xadmin

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('api/alert/<str:info_id>/', alert.AlertInfo.as_view()),
    path('api/alert/', alert.StartInfo.as_view()),
    path('add/', TemplateView.as_view(template_name='add.html')),
    path('list/', TemplateView.as_view(template_name='list.html')),
    path("", TemplateView.as_view(template_name='new.html'))
    # path('new/<int:info_id>', TemplateView.as_view(template_name='new.html')),
]
