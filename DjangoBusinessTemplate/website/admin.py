from django.contrib import admin
from . import models

admin.site.site_header = "ABC Elec Administration"

class EmployeeInline(admin.TabularInline):
    model = models.Employee
    extra = 0

class TestimonialInline(admin.StackedInline):
    model = models.Testimonial
    extra = 0

class ProjectInline(admin.TabularInline):
    model = models.Project
    extra = 0

class ProjectTagInline(admin.StackedInline):
    model = models.Project.tags.through
    extra = 0

class ServiceInline(admin.TabularInline):
    model = models.Service
    extra = 0

class ServiceTagInline(admin.StackedInline):
    model = models.Service.tags.through
    extra = 0

class PackageItemsInline(admin.TabularInline):
    model = models.Package.package_items.through
    extra = 0

class QuoteInline(admin.TabularInline):
    model = models.Quote
    extra = 0

class QuoteServiceInline(admin.TabularInline):
    model = models.Quote.services.through
    extra = 0

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name','job_title', 'updated')
    list_filter = ('job_title',)
    prepopulated_fields = {"slug": ("full_name",)}

class JobTitleAdmin(admin.ModelAdmin):
    inlines = [
        EmployeeInline,
        ]

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title', 'client')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'company', 'updated')
    inlines = [
        TestimonialInline,
        QuoteInline,
        ]

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'author', 'project_url', 'category', 'excerpt', 'status', 'updated', 'published')
    list_filter = ('author', 'category', 'tags')
    prepopulated_fields = {"slug": ("project_title",)}

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'author', 'category', 'excerpt', 'status', 'updated', 'published')
    list_filter = ('author', 'category', 'tags')
    prepopulated_fields = {"slug": ("service_name",)}
    inlines = [
        QuoteServiceInline,
        ]

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ProjectInline,
        ServiceInline,
        ]

class TagAdmin(admin.ModelAdmin):
    inlines = [
        ProjectTagInline,
        ServiceTagInline,
        ]
    exclude = ('tags',)

class PackageAdmin(admin.ModelAdmin):
    list_display = ('package_name', 'price', 'period', 'updated', 'published')
    inlines = [
        PackageItemsInline,
        ]
    exclude = ('package_items'),

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('client', 'start_time', 'submitted')
    list_filter = ('client', 'services')

admin.site.register(models.JobTitle, JobTitleAdmin)
admin.site.register(models.Employee, EmployeeAdmin)

admin.site.register(models.Testimonial, TestimonialAdmin)
admin.site.register(models.Client, ClientAdmin)

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Service, ServiceAdmin)

admin.site.register(models.PackageItem)
admin.site.register(models.Package, PackageAdmin)

admin.site.register(models.Quote, QuoteAdmin)