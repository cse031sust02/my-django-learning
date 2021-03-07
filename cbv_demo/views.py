from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from blog.models import Article
from blog.serializers import ArticleSerializer


class ArticleListView(TemplateView):

    template_name = "articles/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_list'] = Article.objects.all()
        return context

class ArticleDetailView(DetailView):

    model = Article
    template_name = "articles/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context