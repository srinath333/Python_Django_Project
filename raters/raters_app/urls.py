from django.contrib import admin
from django.urls import path
from raters_app import views
from django.conf.urls import include, url
from django.conf import settings
app_name='raters_app'
urlpatterns=[
path("registration/",views.registration)
]