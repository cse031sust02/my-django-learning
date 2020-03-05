from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'content']
    search_fields = ('title', 'pub_date',)
    list_filter = ('title', 'pub_date')
