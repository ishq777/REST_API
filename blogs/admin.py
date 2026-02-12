from django.contrib import admin
from .models import Blog, Comment

class BlogAdmin(admin.ModelAdmin):

    list_display = ['blog_title', 'blog_body' ]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)

# Register your models here.
