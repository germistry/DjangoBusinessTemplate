from .models import Employee, Client, Testimonial, Service, Project, Category, Tag, Package, Post
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from itertools import chain
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
    tags = Tag.tags.get_services_tags()
    return render(request, 'service-detail.html', {'service': service, 'tags': tags})

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

#list view for page 
class PostCategoryListView(ListView):
    template_name = 'postcategory.html'
    context_object_name = 'post_categorylist'

    def get_queryset(self):
        content = {
            'category': self.kwargs['category'],
            'posts': Post.objects.filter(category__category=self.kwargs['category']).filter(status='published')
        }
        return content

def post_detail(request, post):
    post = get_object_or_404(Post, slug=post)
    tags = Tag.tags.get_posts_tags()
    return render(request, 'post-detail.html', {'post': post, 'tags': tags})

#list for menu 
def all_category_list(request):
    all_category_list = Category.categories.all()
    context = {
        "all_category_list": all_category_list,
    }
    return context

class SearchView(ListView):
    template_name = 'search.html'
    count = 0
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        context['cat'] = self.request.GET.get('c')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        cat = request.GET.get('c', None)
        if query is not None:
            post_results = Post.posts.search(query=query, cat=cat)
            service_results = Service.services.search(query=query, cat=cat)
            project_results = Project.projects.search(query=query, cat=cat)
            
            queryset_chain = chain(
                    post_results,
                    service_results,
                    project_results
            )        
            qs = sorted(queryset_chain, 
                        key=lambda instance: instance.pk, 
                        reverse=True)
            self.count = len(qs) # since qs is actually a list
            paginator = Paginator(qs, 6) # 6 posts per page
            page = request.GET.get('page')
            try:
                qs = paginator.page(page)
            except PageNotAnInteger:
                qs = paginator.page(1)
            except EmptyPage:
                qs = paginator.page(paginator.num_pages)
            return qs 
        return Service.objects.none() # have to return some empty model

    
    

    



#def search(request):
#    form = SearchForm()
#    q = ''
#    c = ''
#    query = Q()
#    results = []

#    if 'q' in request.GET:
#        form = SearchForm(request.GET)
#        if form.is_valid():
#            q = form.cleaned_data['q']
#            c = form.cleaned_data['c']
#            if c is not None:
#                query &= Q(category=c) 
#            if q != '':
#                query &= Q(service_name__contains=q)
#            results = Service.objects.filter(query)

#    return render(request, 'search.html', 
#                  {'form': form,
#                   'q': q,
#                   'results': results})

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
