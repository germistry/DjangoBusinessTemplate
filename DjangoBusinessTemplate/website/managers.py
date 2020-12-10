from django.db import models

class EmployeeQuerySet(models.QuerySet):
    def show_homepage(self):
        return self.filter(show_homepage=True)

class EmployeeManager(models.Manager):
    def get_queryset(self):
        return EmployeeQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def all_count(self):
        return self.get_queryset().count()

    def show_homepage(self):
        return self.get_queryset().show_homepage()

class ClientQuerySet(models.QuerySet):
    def display_website(self):
        return self.filter(show_website=True).exclude(company__isnull=True)

class ClientManager(models.Manager):
    def get_queryset(self):
        return ClientQuerySet(self.model, using=self._db)
    
    def all(self):
        return self.get_queryset()

    def all_count(self):
        return self.get_queryset().count()

    def display_website(self):
        return self.get_queryset().display_website()

class TestimonialManager(models.Manager):
    def all(self):
        return self.get_queryset()

class ProjectQuerySet(models.QuerySet):
    def get_authors_projects(self, username):
        return self.filter(user__username, username)

    def get_draft_projects(self):
        return self.filter(status='draft')

    def get_published_projects(self):
        return self.filter(status='published')

class ProjectManager(models.Manager):
    def get_queryset(self):
        return ProjectQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def get_authors_projects(self, username):
        return self.get_queryset().get_authors_projects(username)

    def get_draft_projects(self):
        return self.get_queryset().get_draft_projects()

    def get_published_projects(self):
        return self.get_queryset().get_published_projects()

class ServiceQuerySet(models.QuerySet):
    def get_author_services(self, username):
        return self.filter(author__user__username=username)

    def get_draft_services(self):
        return self.filter(status='draft')

    def get_published_services(self):
        return self.filter(status='published')

class ServiceManager(models.Manager):
    def get_queryset(self):
        return ServiceQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def get_users_services(self, username):
        return self.get_queryset().get_author_services(username)

    def get_draft_services(self):
        return self.get_queryset().get_draft_services()

    def get_published_services(self):
        return self.get_queryset().get_published_services()

class PackageItemManager(models.Manager):
    
    def all(self):
        return self.get_queryset()

class PackageManager(models.Manager):
    
    def all(self):
        return self.get_queryset()

class QuoteQuerySet(models.QuerySet):

    def get_open_quotes(self):
        return self.filter(status='open')

    def get_closed_quotes(self):
        return self.filter(status='closed')

class QuoteManager(models.Manager):
    
    def get_queryset(self):
        return QuoteQuerySet(self.model, using=self._db)
    
    def all(self):
        return self.get_queryset()

    def get_open_quotes(self):
        return self.get_queryset().get_open_quotes()

    def get_closed_quotes(self):
        return self.get_queryset().get_closed_quotes()

class OrderQuerySet(models.QuerySet):

    def get_open_orders(self):
        return self.filter(status='open')

    def get_closed_orders(self):
        return self.filter(status='closed')

class OrderManager(models.Manager):
    
    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def get_open_orders(self):
        return self.get_queryset().get_open_orders()

    def get_closed_orders(self):
        return self.get_queryset().get_closed_orders()

class OrderItemManager(models.Manager):
    
    def all(self):
        return self.get_queryset()

class PostQuerySet(models.QuerySet):
    def get_authors_posts(self, username):
        return self.filter(user__username, username)

    def get_draft_posts(self):
        return self.filter(status='draft')

    def get_published_posts(self):
        return self.filter(status='published')

class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def get_authors_posts(self, username):
        return self.get_queryset().get_authors_posts(username)

    def get_draft_posts(self):
        return self.get_queryset().get_draft_posts()

    def get_published_posts(self):
        return self.get_queryset().get_published_posts()

class CategoryQuerySet(models.QuerySet):
    def get_services_categories(self):
        return self.exclude(services_categories=None)

class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def get_services_categories(self):
        return self.get_queryset().get_services_categories()

class TagManager(models.Manager):
    def all(self):
        return self.get_queryset()

   