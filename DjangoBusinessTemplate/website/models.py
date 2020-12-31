from django.db import models
from django.urls import reverse
from .managers import EmployeeManager, ClientManager, TestimonialManager, ProjectManager, ServiceManager, PackageItemManager, PackageManager, QuoteManager, OrderManager, OrderItemManager, PostManager, TagManager, CategoryManager
from django.utils import timezone
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey

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
    show_website = models.BooleanField(default=False) #determines whether client can be shown on public website for marketing
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

    objects = models.Manager()
    clients = ClientManager()

    class Meta: 
        ordering = ['last_name', 'first_name']

    def __str__(self):
        if self.company is '':
            return '{}, {}'.format(self.last_name, self.first_name)
        return self.company

class Testimonial(models.Model):

    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=40)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True, related_name='testimonials')
    image = models.ImageField(upload_to='testimonials/', default='testimonials/default.jpg', null=True)
    image_caption = models.CharField(max_length=200, blank=True, null=True)
    testimonial_comment = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

    #need the default objects Manager here to make the code in the nested-admin package work properly.
    objects = models.Manager()
    testimonials = TestimonialManager()

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.full_name

class Category(models.Model):

    category = models.CharField(max_length=40)

    objects = models.Manager()
    categories = CategoryManager()

    def __str__(self):
        return self.category

class Tag(models.Model):

    tag = models.CharField(max_length=40)

    objects = models.Manager()
    tags = TagManager()

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects_categories')
    tags = models.ManyToManyField(Tag, related_name='projects_tags')
    image = models.ImageField(upload_to='projects/', default='projects/default.jpg', null=True)
    image_caption = models.CharField(max_length=200, blank=True, null=True)
    project_date = models.DateTimeField(blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='projects_clients')
    content = models.TextField()
    excerpt = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=10, choices=options, default='draft')
    slug = models.SlugField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

    objects = models.Manager()
    projects = ProjectManager()

    def get_absolute_url(self):
        return reverse('project_detail', args=[self.slug])

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services_categories')
    tags = models.ManyToManyField(Tag, related_name='services_tags')
    image = models.ImageField(upload_to='services/', default='services/default.jpg', null=True)
    image_caption = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()
    excerpt = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=10, choices=options, default='draft')
    slug = models.SlugField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

    objects = models.Manager()
    services = ServiceManager()

    def get_absolute_url(self):
        return reverse('service_detail', args=[self.slug])

    class Meta:
        ordering = ['category', 'service_name']

    def __str__(self):
        return self.service_name

class PackageItem(models.Model):

    package_item = models.CharField(max_length=100)

    objects = models.Manager()
    package_items = PackageItemManager()

    def __str__(self):
        return self.package_item

class TaxRate(models.Model):

    tax_rate_name = models.CharField(max_length=3)
    tax_rate = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    objects = models.Manager()

    class Meta:
        ordering = ['tax_rate_name']

    def __str__(self):
        return self.tax_rate_name

class Package(models.Model):

    period_options = (
        ('per month', 'per month'),
        ('per year', 'per year'),
        )

    package_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    tax_rate_name = models.ForeignKey(TaxRate, on_delete=models.PROTECT, related_name='packages_tax_rate_names')
    period = models.CharField(max_length=10, choices=period_options, default='per month')
    description = models.CharField(max_length=254, blank=True, null=True)
    is_top_package = models.BooleanField(default=False)
    package_items = models.ManyToManyField(PackageItem, related_name='package_items')
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

    objects = models.Manager()
    packages = PackageManager()

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

    status_options = (
        ('open', 'Open'),
        ('closed','Closed'),
        )

    #if client already exists pull in their details for quote or else create new client when saving
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='quotes_clients')
    services = models.ManyToManyField(Service, related_name='quotes_services')
    overview = models.TextField()
    budget = models.CharField(max_length=16, choices=budget_options, default='undecided')
    start_time = models.CharField(max_length=16, choices=start_options, default='asap')
    submitted = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=8, choices=status_options, default='open')
    
    #need the default objects Manager here to make the code in the nested-admin package work properly.
    objects = models.Manager()
    quotes = QuoteManager()

    class Meta:
        ordering = ['-status', 'submitted']

    def __str__(self):
        return str(self.id)
    
class Order(models.Model):
    
    status_options = (
        ('open', 'Open'),
        ('closed','Closed'),
        )

    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='orders_clients')
    submitted = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=8, choices=status_options, default='open')

    #need the default objects Manager here to make the code in the nested-admin package work properly.
    objects = models.Manager()
    orders = OrderManager()

    class Meta:
        ordering = ['client', '-status', 'submitted']

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items_orders')
    package = models.ForeignKey(Package, on_delete=models.PROTECT, related_name='order_items_packages')
    quantity = models.IntegerField()

    #need the default objects Manager here to make the code in the nested-admin package work properly.
    objects = models.Manager()
    order_items = OrderItemManager()

    def __str__(self):
        return str(self.id)

class Post(models.Model):
    
    options = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    post_title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_authors')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts_categories')
    tags = models.ManyToManyField(Tag, related_name='posts_tags')
    image = models.ImageField(upload_to='posts/', default='posts/default.jpg', null=True)
    image_caption = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()
    excerpt = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=10, choices=options, default='draft')
    slug = models.SlugField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

    objects = models.Manager()
    projects = PostManager()

    def get_absolute_url(self):
        return reverse('post:single', args=[self.slug])

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.post_title

class Comment(MPTTModel):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_posts')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    display_name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ['published']

    def __str__(self):
        return 'Comment by {}'.format(self.display_name)