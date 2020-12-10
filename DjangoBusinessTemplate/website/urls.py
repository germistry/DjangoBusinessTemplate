from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('team/', views.team, name="team"),
    path('about/', views.about, name="about"),
    path('services/', views.allservices, name="allservices"),
    path('services/<category>/', views.ServiceCategoryListView.as_view(), name='services_categories'),
    path('service/<slug:service>/', views.service_detail, name="service_detail"),
    path('allprojects.html', views.allprojects, name="allprojects"),
]
