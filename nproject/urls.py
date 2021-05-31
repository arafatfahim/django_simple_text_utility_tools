"""nproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),
    #path('captf', views.capitalize_first, name='capitalize_first'),
    #path('nlr', views.newline_remove, name='newline_remove'),
    #path('sr', views.space_remove, name='spaceremove'),
    #path('chc', views.charecter_counter, name='charecter_counter'),
    #path('about/', views.about, name='about'),
    #path('contact/', views.contact, name='contact'),
]
