from django.urls import path
from AppTwo import views

app_name = 'AppTwo'

urlpatterns = [
    path('help/', views.Help, name='help'),
    path('register/', views.register_form, name='register'),
    path('login/', views.user_login, name='login')
]