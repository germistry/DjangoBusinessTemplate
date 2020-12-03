from django.db import models
from django.urls import reverse
from .managers import EmployeeManager, ClientManager, TestimonialManager, ProjectManager
from django.utils import timezone
from django.contrib.auth.models import User

class JobTitle(models.Model):

    title = models.CharField(max_length=40)
    
    def __str__(self):
        return self.title

class Employee(models.Model):
    
    full_name = models.CharField(max_length=100)
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE, related_name='titles')
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

    company = models.CharField(max_length=50)
    company_url = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='clients/', default='clients/default.png', null=True)
    image_caption = models.CharField(max_length=200, blank=True, null=True)
    contact_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=200, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

    clients = ClientManager()

    class Meta: 
        ordering = ['-published']

    def __str__(self):
        return self.company

class Testimonial(models.Model):

    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=40)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True, related_name='client')
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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_authors')
    project_url = models.URLField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    tags = models.ManyToManyField(Tag, related_name='tags')
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