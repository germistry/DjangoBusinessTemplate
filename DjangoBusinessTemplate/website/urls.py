from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('team.html', views.team, name="team"),
    path('about.html', views.about, name="about"),
    path('allservices.html', views.allservices, name="allservices"),
]
