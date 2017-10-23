# coding:utf-8
from django import forms
from pagedown.widgets import AdminPagedownWidget
from models import Blog


class CommentForm(forms.Form):
        name = forms.CharField(label='称呼', max_length=16, error_messages={
            'required': '请填写您的称呼',
            'max_length': '称呼太长咯'
        })
        email = forms.EmailField(label='邮箱', error_messages={
            'required': '请填写您的邮箱',
            'invalid': '邮箱格式不正确'
        })

        content = forms.CharField(label='评论内容', error_messages={
            'required': '请填写您的评论内容！',
            'max_length': '评论内容太长咯'
        })


class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget(), label='博客正文')

    class Meta:
        model = Blog
        fields = '__all__'

