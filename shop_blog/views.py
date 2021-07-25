from django.http import Http404
from django.shortcuts import render
from .models import Article

# Create your views here.


def blog(request):
    articles = Article.objects.filter(active=True).order_by('-id').all()

    context = {
        'title': 'بلاگ | فروشگاه ووگا فودز',
        'slider_title': 'بلاگ فروشگاه',
        'slider_text': 'مقالات',
        'articles': articles
    }
    return render(request, 'blog/blog.html', context)


def article(request, *args, **kwargs):
    article_id = kwargs.get('articleId')
    active_article = Article.objects.filter(id=article_id, active=True).first()
    if article is None:
        raise Http404

    context = {
        'title': 'بلاگ | فروشگاه ووگا فودز',
        'slider_title': 'بلاگ فروشگاه',
        'slider_text': active_article.title,
        'article': active_article
    }
    return render(request, 'blog/article.html', context)


def search(request):
    query = request.GET.get('aq')
    articles = Article.objects.search(query=query)
    if articles is None:
        articles = Article.objects.filter(active=True).all()

    context = {
        'title': 'بلاگ | فروشگاه ووگا فودز',
        'slider_title': 'بلاگ فروشگاه',
        'slider_text': 'مقالات',
        'articles': articles
    }
    return render(request, 'blog/blog.html', context)
