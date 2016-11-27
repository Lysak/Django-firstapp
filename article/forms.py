# -*- coding: utf-8 -*-
__author__ = 'lysak'

from django.forms import ModelForm
from article.models import Comments

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        #fields = "__all__"
        exclude = ['comments_article']