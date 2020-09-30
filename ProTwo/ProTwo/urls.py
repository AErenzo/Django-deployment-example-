"""ProTwo URL Configuration

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
from django.urls import path, include
from AppTwo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('AppTwo/', include('AppTwo.urls')),
    path('users/', views.users, name='users'),
    path('project_idea_form/', views.project_model_form, name='project_form'),
    path('projects/', views.submitted_projects, name='projects'),
    path('logout/', views.user_logout, name='logout'),
    path('contact/', views.contact_form, name='contact form'),
    path('sign_up/', views.sign_up_modelform, name='Sign Up'),
    path('admin/', admin.site.urls),
]
