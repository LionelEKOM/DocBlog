from django.contrib import admin
from .models import BlogPost, Category

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "date")
admin.site.register(BlogPost, BlogPostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)
admin.site.register(Category, CategoryAdmin)