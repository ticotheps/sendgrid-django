"""hello_sendgrid URL Configuration

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
#-------------------------------------------------------------

# # Newer code from django v3.0.5
# from django.contrib import admin
# from django.urls import path

# from hello_sendgrid import views

# # Newer code from django v3.0.5
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('sendgrid/', index, name='sendgrid'),
# ]

#-------------------------------------------------------------

# Older code from 04/05/19
from django.conf.urls import url
from django.contrib import admin

from .views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sendgrid/', index, name='sendgrid'),
]


