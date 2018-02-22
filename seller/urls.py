from django.conf.urls import url
from django.urls import path
from seller import views

app_name = 'sellers'
urlpatterns = [
    path("search", views.search)
]
