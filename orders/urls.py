from django.conf.urls import url
from django.urls import path
from orders import views

app_name = 'orders'
urlpatterns = [
    path('entry', views.entry),
    path('assign', views.assign),
    path('update', views.update),
    path('search', views.search),
]
