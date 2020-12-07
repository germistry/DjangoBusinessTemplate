from .models import Employee, Client, Testimonial, Service
#from datetime import datetime
#from django.http import HttpRequest

from django.shortcuts import render

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
