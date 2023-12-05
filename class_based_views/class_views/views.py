from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Article

class ArticleDetailView(DetailView):
    model = Article