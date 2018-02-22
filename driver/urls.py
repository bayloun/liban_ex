from django.conf.urls import url
from django.urls import path
from driver import views

app_name = 'drivers'
urlpatterns = [
    path('checkin', views.checkin)
]
