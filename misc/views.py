from django.core import serializers
from django.http import HttpResponse

from blog.models import Article


def serializer_demo(request):
    articles = Article.objects.all()
    # serialize queryset
    article_list = serializers.serialize('json', articles)
    return HttpResponse(article_list, content_type="text/json-comment-filtered")
