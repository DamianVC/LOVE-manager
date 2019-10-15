"""manager URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples
--------
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('manager/admin/', admin.site.urls),
    path('manager/test/', TemplateView.as_view(template_name="test.html")),
    path('manager/login/', TemplateView.as_view(template_name="registration/login.html")),
    path('manager/api/', include('api.urls')),
    path('manager/ui_framework/', include('ui_framework.urls')),
]
