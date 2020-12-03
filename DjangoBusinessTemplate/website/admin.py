from django.contrib import admin
from . import models

admin.site.site_header = "ABC Elec Administration"

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name','job_title', 'updated')
    list_filter = ('job_title',)
    prepopulated_fields = {"slug": ("full_name",)}

class EmployeeInline(admin.TabularInline):
    model = models.Employee
    extra = 0

class JobTitleAdmin(admin.ModelAdmin):
    inlines = [
        EmployeeInline,
        ]

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title', 'client')

class TestimonialInline(admin.StackedInline):
    model = models.Testimonial
    extra = 0

class ClientAdmin(admin.ModelAdmin):
    list_display = ('company', 'company_url', 'contact_name', 'updated')
    inlines = [
        TestimonialInline,
        ]

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'author', 'project_url', 'category', 'excerpt', 'status', 'updated', 'published')
    list_filter = ('author', 'category', 'tags')
    prepopulated_fields = {"slug": ("project_title",)}

class ProjectCategoryInline(admin.TabularInline):
    model = models.Project
    extra = 0

class ProjectTagInline(admin.StackedInline):
    model = models.Project.tags.through
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ProjectCategoryInline
        ]

class TagAdmin(admin.ModelAdmin):
    inlines = [
        ProjectTagInline
        ]
    exclude = ('tags',)

admin.site.register(models.JobTitle, JobTitleAdmin)
admin.site.register(models.Employee, EmployeeAdmin)

admin.site.register(models.Testimonial, TestimonialAdmin)
admin.site.register(models.Client, ClientAdmin)

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Project, ProjectAdmin)
