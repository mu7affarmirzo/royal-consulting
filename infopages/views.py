from django.shortcuts import render, redirect, get_object_or_404
from operator import attrgetter

from django.db.models import Q
from django.http import HttpResponse

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.views.generic import TemplateView
from .models import NewsModel, InfoPageModel
from wedo.models import *
from asia.models import *
from django.utils.translation import ugettext_lazy as _

NEWS_PER_PAGE = 6

def home_screen_view(request, *args, **kwargs):

    wedo = InformationPagesModel.objects.all()
    asia = CentralAsiaPagesModel.objects.all()

    homenews = list(NewsModel.objects.all())[:4]
    context = {
        'wedo': wedo,
        'homenews': homenews,
        'asia': asia
    }

    return render(request, "pages/index.html", context)

def detail_news_view(request, slug):

    context = {}

    posts = get_object_or_404(NewsModel, slug=slug)
    context['posts'] = posts

    return render(request, 'pages/news_detail.html', context)






class ComingSoonView(TemplateView):
    template_name = 'pages/comingsoon.html'

class FaqView(TemplateView):
    template_name = 'pages/faq.html'

class HomeScreenView(TemplateView):
    template_name = 'pages/index.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class CentralAsiaView(TemplateView):
    template_name = 'pages/competence.html'

class RerourcesView(TemplateView):
    template_name = 'pages/recourses.html'

class ContactsView(TemplateView):
    template_name = 'pages/contacts.html'







def news_list_view(request, *args, **kwargs):
    context = {}

    query = ""
    query = request.GET.get('q', '')
    context['query'] = str(query)

    news = sorted(get_blog_queryset(query), key=attrgetter('date_published'), reverse=True)

    # Pagination
    page = request.GET.get('page', 1)
    news_paginator = Paginator(news, NEWS_PER_PAGE)

    try:
        news = news_paginator.page(page)
    except PageNotAnInteger:
        news = news_paginator.page(NEWS_PER_PAGE)
    except EmptyPage:
        news = news_paginator.page(news_paginator.num_pages)

    context['news'] = news

    return render(request, "pages/news_list.html", context)


def individual_view(request, slug):

    context = {}

    posts = get_object_or_404(InfoPageModel, slug=slug)
    context['posts'] = posts

    return render(request, 'pages/individual.html', context)



def get_blog_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        news = NewsModel.objects.filter(
                Q(title__icontains=q) |
                Q(body__icontains=q)
            ).distinct()

        for new in news:
            queryset.append(new)

    return list(set(queryset))

