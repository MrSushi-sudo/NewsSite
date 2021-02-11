from django.views import generic
from .forms import NewsForm
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from .models import News


def redirect_view(request):
    response = redirect('news/')
    return response


class NewsList(generic.ListView):
    queryset = News.objects.get_queryset().order_by('id')
    template_name = 'home.html'
    paginate_by = 10

    def get_paginate_by(self, queryset):
        self.paginate_by = self.request.GET.get('paginate_by', self.paginate_by)
        return self.paginate_by


class NewsDetail(generic.DetailView):
    model = News
    template_name = 'news_detail.html'


class NewsCreateView(CreateView):
    template_name = 'create.html'
    form_class = NewsForm

