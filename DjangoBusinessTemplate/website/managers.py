from django.db import models

class EmployeeQuerySet(models.QuerySet):
    def show_homepage(self):
        return self.filter(show_homepage=True)

class EmployeeManager(models.Manager):
    def get_queryset(self):
        return EmployeeQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def show_homepage(self):
        return self.get_queryset().show_homepage()

class ClientManager(models.Manager):
    def all(self):
        return self.get_queryset()

class TestimonialManager(models.Manager):
    def all(self):
        return self.get_queryset()

class ProjectQuerySet(models.QuerySet):
    def get_authors_projects(self, username):
        return self.filter(author__username, username)

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