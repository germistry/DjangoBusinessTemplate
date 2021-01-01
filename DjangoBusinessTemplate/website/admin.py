from django.contrib import admin
from . import models
from nested_admin import NestedModelAdmin, NestedTabularInline
from mptt.admin import MPTTModelAdmin

admin.site.site_header = "ABC Elec Administration"

class EmployeeInline(admin.TabularInline):
    model = models.Employee
    extra = 0

class TestimonialInline(NestedTabularInline):
    model = models.Testimonial
    extra = 0

class ProjectInline(NestedTabularInline):
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

class PackageInline(admin.TabularInline):
    model = models.Package
    extra = 0

class QuoteInline(NestedTabularInline):
    model = models.Quote
    extra = 0

class QuoteServiceInline(admin.TabularInline):
    model = models.Quote.services.through
    extra = 0

class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    extra = 0

class OrderDetailsInline(NestedTabularInline):
    model = models.OrderItem
    extra = 0

class OrderInline(NestedTabularInline):
    model = models.Order
    extra = 0
    inlines = [
        OrderDetailsInline,
        ]

class PostInline(admin.TabularInline):
    model = models.Post
    extra = 0

class PostTagInline(admin.StackedInline):
    model = models.Post.tags.through
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

class ClientAdmin(NestedModelAdmin):
    list_display = ('last_name', 'first_name', 'company', 'updated')
    inlines = [
        TestimonialInline,
        ProjectInline,
        QuoteInline,
        OrderInline,
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
        PostInline,
        ]

class TagAdmin(admin.ModelAdmin):
    inlines = [
        ProjectTagInline,
        ServiceTagInline,
        PostTagInline,
        ]
    exclude = ('tags',)

class TaxRateAdmin(admin.ModelAdmin):
    inlines = [
        PackageInline,
        ]

class PackageAdmin(admin.ModelAdmin):
    list_display = ('package_name', 'price', 'tax_rate_name', 'period', 'is_top_package', 'updated', 'published')
    inlines = [
        PackageItemsInline,
        OrderItemInline,
        ]
    exclude = ('package_items'),

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('client', 'start_time', 'submitted')
    list_filter = ('client', 'services')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'submitted', 'status')
    list_filter = ('client', 'status')
    inlines = [
        OrderItemInline,
        ]

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'author', 'category', 'excerpt', 'status', 'updated', 'published')
    list_filter = ('author', 'category', 'tags')
    prepopulated_fields = {"slug": ("post_title",)} 

admin.site.register(models.JobTitle, JobTitleAdmin)
admin.site.register(models.Employee, EmployeeAdmin)

admin.site.register(models.Testimonial, TestimonialAdmin)
admin.site.register(models.Client, ClientAdmin)

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Service, ServiceAdmin)

admin.site.register(models.TaxRate, TaxRateAdmin)
admin.site.register(models.PackageItem)
admin.site.register(models.Package, PackageAdmin)

admin.site.register(models.Quote, QuoteAdmin)
admin.site.register(models.Order, OrderAdmin)

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, MPTTModelAdmin)