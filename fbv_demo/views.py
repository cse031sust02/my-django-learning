from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


from blog.models import Article
from blog.serializers import ArticleSerializer


def article_list(request):
    article_list = Article.objects.order_by('-pub_date')
    context = {'article_list': article_list}
    return render(request, 'articles/index.html', context)


def article_details(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/detail.html', {'article': article})
