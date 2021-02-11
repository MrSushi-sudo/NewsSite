from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_date', 'body_text', 'image')
    list_filter = ('title',)
    search_fields = ['title', ]


admin.site.register(News, NewsAdmin)

