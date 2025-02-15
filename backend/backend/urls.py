"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from .views import google_auth_callback

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),  # Allauth
    path('api/auth/', include('dj_rest_auth.urls')),  # Auth endpoints
    path('api/auth/google/', include('allauth.urls')),  # Google Auth
    path("api/auth/google/callback/", google_auth_callback, name="google_auth_callback"),
]

