"""CP2 URL Configuration

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
from CP2.settings import STATICFILES_DIRS, STATIC_URL
from django.contrib import admin
from django.urls import path ,include

admin.site.site_header = "Krishi Pradhan Admin"
admin.site.site_title = "Krishi Pradhan Admin Portal"
admin.site.index_title = "Welcome to Krishi Pradhan Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Krishi_Pradhan.urls')),
   
]
