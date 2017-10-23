# coding=utf8
from django.shortcuts import render
from BlogApp.models import *
from django.shortcuts import render_to_response
from django.http import Http404
from BlogApp.forms import CommentForm


# Create your views here.
def get_blog(request):
    blogs = Blog.objects.all().order_by('-created')
    return render_to_response('index.html', {'blogs': blogs})


def get_category(request, cg):
    # get all blog of catagory
    try:
        category = Category.objects.filter(name=cg)[0]
        # get the category ID according to the category name from the table
        blog = Blog.objects.filter(category_id=category).order_by('-created')
    except Blog.DoesNotExist:
        raise Http404
    return render(request, 'category_list.html', {'blog': blog})


def get_detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        tags = blog.tags.all()
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
        
    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form,
        'tags': tags
    }
    return render(request, 'base.html', ctx)
