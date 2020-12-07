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
    
    def get_category_projects(self, category):
        return self.filter(project_category__category__category, category)

    def get_tag_projects(self, tag):
        return self.filter(project_tag__tag__tag, tag)

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

    def get_category_projects(self, category):
        return self.get_queryset().get_category_projects(category)

    def get_tag_projects(self, tag):
        return self.get_queryset().get_tag_projects(tag)

class ServiceQuerySet(models.QuerySet):
    def get_authors_services(self, username):
        return self.filter(user__username, username)

    def get_draft_services(self):
        return self.filter(status='draft')

    def get_published_services(self):
        return self.filter(status='published')

    def get_category_services(self, category):
        return self.filter(service_category__category__category, category)

    def get_tag_services(self, tag):
        return self.filter(service_tag__tag__tag, tag)

class ServiceManager(models.Manager):
    def get_queryset(self):
        return ServiceQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def get_authors_services(self, username):
        return self.get_queryset().get_authors_services(username)

    def get_draft_services(self):
        return self.get_queryset().get_draft_services()

    def get_published_services(self):
        return self.get_queryset().get_published_services()

    def get_category_services(self, category):
        return self.get_queryset().get_category_services(category)

    def get_tag_services(self, tag):
        return self.get_queryset().get_tag_services(tag)

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
    
    def get_category_posts(self, category):
        return self.filter(post_category__category__category, category)

    def get_tag_posts(self, tag):
        return self.filter(post_tag__tag__tag, tag)

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

    def get_category_posts(self, category):
        return self.get_queryset().get_category_posts(category)

    def get_tag_posts(self, tag):
        return self.get_queryset().get_tag_posts(tag)
