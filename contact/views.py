from django.shortcuts import render

from articles.models import Article
from contact.models import Contact


def home_page(request):
    model = Contact()
    if request.POST:
        model.name = request.POST.get('name')
        model.tell = request.POST.get('tell')
        model.email = request.POST.get('email')
        model.message = request.POST.get('message')
        model.save()
    articles = Article.objects.all()
    ctx = {
        "articles": articles
    }
    return render(request, 'index.html', ctx)


def about_page(request):
    return render(request, 'about.html')


def work_page(request):
    return render(request, 'work.html')


# def blog_page(request):
#     articles = Article.objects.all()
#     ctx = {
#         "articles": articles
#     }
#     return render(request, 'index.html', ctx)


def contact_page(request):
    model = Contact()
    if request.POST:
        model.name = request.POST.get('name')
        model.tell = request.POST.get('tell')
        model.email = request.POST.get('email')
        model.message = request.POST.get('message')
        model.save()
    return render(request, 'contact.html')
