from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), #the empty string means the url in this app will be mapped/appended to the project/root url
]