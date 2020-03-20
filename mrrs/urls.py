from django.conf.urls import url
from . import views

urlpatterns = [
    url('room', views.room, name='room'),
    url(r'^$', views.mrrs, name='mrrs'),
]
