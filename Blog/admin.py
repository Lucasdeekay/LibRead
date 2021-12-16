from django.contrib import admin

from Blog.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'article', 'date')


admin.site.register(Blog, BlogAdmin)
