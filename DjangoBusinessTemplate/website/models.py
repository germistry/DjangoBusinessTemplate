from django.db import models
from django.urls import reverse
from .managers import EmployeeManager, ClientManager, TestimonialManager, ProjectManager, ServiceManager
from django.utils import timezone
from django.contrib.auth.models import User

class JobTitle(models.Model):

    title = models.CharField(max_length=40)
    
    def __str__(self):
        return self.title

class Employee(models.Model):
    
    full_name = models.CharField(max_length=100)
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE, related_name='employees')
    image = models.ImageField(upload_to='employees/', default='employees/default.jpg', null=True)
    image_caption = models.CharField(max_length=100)
    about = models.TextField(blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    show_homepage = models.BooleanField() #may use this boolean on homepage if needed
    slug = models.SlugField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    
    employees = EmployeeManager()

    def get_absolute_url(self):
        return reverse('employee:single', args=[self.slug])

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return self.full_name

class Client(models.Model):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=200, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    company_url = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='clients/', default='clients/default.png', null=True)
    image_caption = models.CharField(max_length=200, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

    clients = ClientManager()

    class Meta: 
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)

class Testimonial(models.Model):

    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=40)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True, related_name='testimonials')
    image = models.ImageField(upload_to='testimonials/', default='testimonials/default.jpg', null=True)
    image_caption = models.CharField(max_length=200, blank=True, null=True)
    testimonial_comment = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

    testimonials = TestimonialManager()

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.full_name

class Category(models.Model):

    category = models.CharField(max_length=40)

    def __str__(self):
        return self.category

class Tag(models.Model):

    tag = models.CharField(max_length=40)

    def __str__(self):
        return self.tag

class Project(models.Model):

    options = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    project_title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_authors')
    project_url = models.URLField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects_categorys')
    tags = models.ManyToManyField(Tag, related_name='projects_tags')
    image = models.ImageField(upload_to='projects/', default='projects/default.jpg', null=True)
    image_caption = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()
    excerpt = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=10, choices=options, default='draft')
    slug = models.SlugField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

    projects = ProjectManager()

    def get_absolute_url(self):
        return reverse('project:single', args=[self.slug])

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.project_title

class Service(models.Model):

    options = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    service_name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='services_authors')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services_categorys')
    tags = models.ManyToManyField(Tag, related_name='services_tags')
    image = models.ImageField(upload_to='services/', default='services/default.jpg', null=True)
    image_caption = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()
    excerpt = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=10, choices=options, default='draft')
    slug = models.SlugField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

    services = ServiceManager()

    def get_absolute_url(self):
        return reverse('service:single', args=[self.slug])

    class Meta:
        ordering = ['category', 'service_name']

    def __str__(self):
        return self.service_name

class PackageItem(models.Model):

    package_item = models.CharField(max_length=100)

    def __str__(self):
        return self.package_item


class Package(models.Model):

    period_options = (
        ('per month', 'per month'),
        ('per year', 'per year'),
        )

    package_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    period = models.CharField(max_length=10, choices=period_options, default='per month')
    description = models.CharField(max_length=254, blank=True, null=True)
    package_items = models.ManyToManyField(PackageItem, related_name='package_items')
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

    @property
    def price_display(self):
        return "$%s" % self.price

    class Meta:
        ordering = ['price']

    def __str__(self):
        return self.package_name

class Quote(models.Model):

    budget_options = (
        ('500-1000', '$500 - $1000'),
        ('1000-4000', '$1000 - $4000'),
        ('4000-8000', '$4000 - $8000'),
        ('undecided', 'undecided'),
        )

    start_options = (
        ('asap','ASAP'),
        ('1-2','1-2 weeks'),
        ('2-4','2-4 weeks'),
        ('4plus','4+ weeks'),
        )
    #if client already exists pull in their details for quote or else create new client when saving
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='quotes_clients')
    services = models.ManyToManyField(Service, related_name='quotes_services')
    overview = models.TextField()
    budget = models.CharField(max_length=16, choices=budget_options, default='undecided')
    start_time = models.CharField(max_length=16, choices=start_options, default='asap')
    submitted = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['submitted']

    def __str__(self):
        return '{} quote {}'.format(self.client, self.submitted)
    
