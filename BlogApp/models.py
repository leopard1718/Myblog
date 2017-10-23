# coding:utf8
from django.db import models
from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget
from django import forms


# Create your models here.

class Category(models.Model):
    """
    博客分类
    """
    name = models.CharField('名称', max_length=30)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    """
    博客标签
    """
    name = models.CharField('名称', max_length=16)

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    """
    博客
    """
    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    abstract = models.CharField('摘要', max_length=54, blank=True, null=True,
                                help_text="可选，如若为空则摘取正文前54个字符")
    content = models.TextField('博客正文')
    created = models.DateTimeField('发布时间', auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    """
    评论
    """
    blog = models.ForeignKey(Blog, verbose_name='博客')
    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=240)
    created = models.DateTimeField('发布时间', auto_now_add=True)

    def __unicode__(self):
        return self.content
