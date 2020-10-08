"""project23 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from app import views

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('CBV_template/',views.CBV_template.as_view(),name='CBV_template'),
    path('CBV_templateview/',TemplateView.as_view(template_name='CBV_template.html'),name='CBV_templateview'),
    
    path('CBV_contexttemplate/',views.CBV_contexttemplate.as_view(),name='CBV_contexttemplate'),
    
    path('CBV_formview/',views.CBV_formview.as_view(),name='CBV_formview'),
    path('CBV_modelform/',views.CBV_modelform.as_view(),name='CBV_modelform'),
    path('CBV_listview/',views.CBV_listview.as_view(),name='CBV_listview'),


]
