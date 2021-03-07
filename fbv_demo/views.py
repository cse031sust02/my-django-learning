from django.http import HttpResponse


from blog.models import Article
from blog.serializers import ArticleSerializer


def artcile_list(request):
    artcile_list = Article.objects.order_by('-pub_date')
    output = ', '.join([q.title for q in artcile_list])
    return HttpResponse(output)
