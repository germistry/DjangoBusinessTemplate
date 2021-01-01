from .models import Employee, Client, Testimonial, Service, Project, Category, Package, Post
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
#from datetime import datetime
#from django.http import HttpRequest

def home(request):
    return render(request, 'home.html', {})

def team(request):
    employees = Employee.employees.all()
    return render(request, 'team.html', {'employees': employees})

def about(request):
    clients = Client.clients.display_website()
    client_count = Client.clients.all_count()
    employee_count = Employee.employees.all_count()
    testimonials = Testimonial.testimonials.all()
    return render(request, 'about.html', {'clients': clients, 'client_count': client_count, 'employee_count': employee_count, 'testimonials': testimonials})

def allservices(request):
    services = Service.services.get_published_services()
    return render(request, 'allservices.html', {'services': services})

def service_detail(request, service):
    service = get_object_or_404(Service, slug=service)
    return render(request, 'service-detail.html', {'service': service})

#list view for page 
class ServiceCategoryListView(ListView):
    template_name = 'servicecategory.html'
    context_object_name = 'service_categorylist'

    def get_queryset(self):
        content = {
            'category': self.kwargs['category'],
            'services': Service.objects.filter(category__category=self.kwargs['category']).filter(status='published')
        }
        return content
#list for menu 
def services_category_list(request):
    services_category_list = Category.categories.get_services_categories()
    context = {
        "services_category_list": services_category_list,
    }
    return context

def allprojects(request):
    projects = Project.projects.get_published_projects()
    clients = Client.clients.display_website()
    return render(request, 'allprojects.html', {'projects': projects, 'clients': clients})

def project_detail(request, project):
    project = get_object_or_404(Project, slug=project)
    return render(request, 'project-detail.html', {'project': project})

#list view for page 
class ProjectCategoryListView(ListView):
    template_name = 'projectcategory.html'
    context_object_name = 'project_categorylist'

    def get_queryset(self):
        content = {
            'category': self.kwargs['category'],
            'projects': Project.objects.filter(category__category=self.kwargs['category']).filter(status='published')
        }
        return content
#list for menu 
def projects_category_list(request):
    projects_category_list = Category.categories.get_projects_categories()
    context = {
        "projects_category_list": projects_category_list,
    }
    return context

def allpackages(request):
    packages = Package.packages.all()
    return render(request, 'pricing.html', {'packages': packages})

def allposts(request):
    posts = Post.posts.get_published_posts()
    return render(request, 'allposts.html', {'posts': posts})

def post_detail(request, post):
    post = get_object_or_404(Post, slug=post)
    return render(request, 'post-detail.html', {'post': post})

#def contact(request):
#    """Renders the contact page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/contact.html',
#        {
#            'title':'Contact',
#            'message':'Your contact page.',
#            'year':datetime.now().year,
#        }
#    )

#def about(request):
#    """Renders the about page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/about.html',
#        {
#            'title':'About',
#            'message':'Your application description page.',
#            'year':datetime.now().year,
#        }
#    )
