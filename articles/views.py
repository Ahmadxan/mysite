from django.shortcuts import render
from .models import Article, Comment


def blog_page(request):
    articles = Article.objects.all()
    ctx = {
        "articles": articles
    }
    return render(request, 'blog.html', ctx)