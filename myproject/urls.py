"""
Main Url
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basic-auth/', include("basicauthentication.urls"))
]
