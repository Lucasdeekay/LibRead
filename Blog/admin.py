from django.contrib import admin

from Blog.models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'article', 'date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('clientele', 'comment', 'date')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
