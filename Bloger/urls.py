"""Bloger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authView
from loginRegister import views
from loginRegister import forms

urlpatterns = [
    path('@dmin/', include('Admin.urls')),
    path('blog/', include('blog.urls')),
    path('', authView.LoginView.as_view(authentication_form=forms.AuthFormCheckStatus), name='login'),
    path('admin/', authView.LoginView.as_view(authentication_form=forms.AuthFormCheckStatus), name='login'),
    path('logout/', authView.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('loginRegister/', include('loginRegister.urls')),
    path('summernote/', include('django_summernote.urls')),#summernote
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
