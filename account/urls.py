"""index URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import  path
from django.contrib.auth import views as auth_views
from . import views
app_name="account"
urlpatterns = [
    path('registrationUser/',views.UserCreationForm.as_view(), name="registrationUser"),
    path('<int:pk>/edit/',views.AccountUpdateView.as_view(), name="updateAccount"),
    path('login/',auth_views.LoginView.as_view(),name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name="logged_out"),
    path('<int:pk>/', views.profile, name='profile'),
     path('<int:pk>/delete/',views.AccountDeleteView.as_view(),name='account_delete'),
]