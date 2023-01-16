from django.contrib import admin
from django.urls import path

from .views.home import index
from .views.redirect import urlredirect

urlpatterns = [
    path('',index,name='homepage'),
    path('<str:keyword>',urlredirect,name="redirect"),
]
