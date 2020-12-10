from .models import Employee, Client, Testimonial, Service, Project, Category
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

def allprojects(request):
    projects = Project.projects.get_published_projects()
    clients = Client.clients.display_website()
    return render(request, 'allprojects.html', {'projects': projects, 'clients': clients})

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
