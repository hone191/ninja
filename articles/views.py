from django.shortcuts import render
from nin.articles.models import Article


def article_list(request):
    articles = Article.objects.all().order_by('date');
    return render(request, 'articles/article_list.html', {'articles': articles})


def article_details(request, slug):

    #return HttpResponse(slug)
    article = Article.objects.get(slug = slug)
    return render(request, 'articles/article_detail.html', {'article': article})
