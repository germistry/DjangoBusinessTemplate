from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('team/', views.team, name="team"),
    path('about/', views.about, name="about"),
    path('services/', views.allservices, name="allservices"),
    path('services/<category>/', views.ServiceCategoryListView.as_view(), name='services_categories'),
    path('service/<slug:service>/', views.service_detail, name="service_detail"),
    path('projects/', views.allprojects, name="allprojects"),
    path('projects/<category>/', views.ProjectCategoryListView.as_view(), name='projects_categories'),
    path('project/<slug:project>/', views.project_detail, name="project_detail"),
    path('pricing/', views.allpackages, name="allpackages"),
    path('posts/', views.allposts, name="allposts"),
    path('posts/<category>/', views.PostCategoryListView.as_view(), name='posts_categories'),
    path('post/<slug:post>/', views.post_detail, name="post_detail"),
    path('search/', views.SearchView.as_view(), name="search"),
    path('categories/', views.categories, name="categories"),
    path('tags/', views.tags, name="tags"),
]