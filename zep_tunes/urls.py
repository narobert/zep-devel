"""zep_tunes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

# Imported views from apps
from vkconfig import views as vkconfig_views

urlpatterns = [
    url(r'^$', vkconfig_views.dashboard, name='get_dashboard'),
    url(r'^search/', vkconfig_views.search, name='search'),
    url(r'^api/', include('api.urls')),

    # Admin page to view models
    url(r'^admin/', admin.site.urls),
]