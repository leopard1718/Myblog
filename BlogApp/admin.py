from django.contrib import admin
from models import Comment, Category, Tag, Blog
from forms import BlogForm

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    form = BlogForm
    list_display = ('title', 'author', 'category', 'created')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'name', 'content', 'created')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register([Tag, Category])
