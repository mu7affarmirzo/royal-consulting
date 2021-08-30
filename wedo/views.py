from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import *

NEWS_PER_PAGE = 12


def news_detial_view(request, slug):

    context = {}
    pages = OpportunitiesModel.objects.all()
    posts = get_object_or_404(NewsModel, slug=slug)
    context = {
        'posts': posts,
        'pages': pages,
    }

    return render(request, 'details_page.html', context)



def photo_bank_view(request, *args, **kwargs):

    context = {}

    photos = PhotoBankModel.objects.all()
    context['photos'] = photos

    return render(request, 'photo_bank.html', context)


def details_page_view(request, slug):

    context = {}
    pages = InformationPagesModel.objects.all()

    posts = get_object_or_404(InformationPagesModel, slug=slug)
    # context['posts'] = posts
    context = {
        'posts': posts,
        'pages': pages,
    }

    return render(request, 'details_page.html', context)


def details_wedo_page_view(request, slug):

    context = {}
    pages = OpportunitiesModel.objects.all()
    posts = get_object_or_404(OpportunitiesModel, slug=slug)
    context = {
        'posts': posts,
        'pages': pages,
    }

    return render(request, 'opp_details_page.html', context)

def news_page_view(request, slug):

    context = {}
    pages = OpportunitiesModel.objects.all()
    posts = get_object_or_404(OpportunitiesModel, slug=slug)
    context = {
        'posts': posts,
        'pages': pages,
    }

    return render(request, 'opp_details_page.html', context)


# def news_detial_view(request, slug):
#
#     context = {}
#     pages = OpportunitiesModel.objects.all()
#     posts = get_object_or_404(NewsModel, slug=slug)
#     context = {
#         'posts': posts,
#         'pages': pages,
#     }
#
#     return render(request, 'details_page.html', context)


def news_list_view(request, *args, **kwargs):
    context = {}

    query = ""
    query = request.GET.get('q', '')
    context['query'] = str(query)

    news = sorted(get_news_queryset(query), key=attrgetter('date_published'), reverse=True)

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

    return render(request, "news.html", context)



def get_news_queryset(query=None):
    news_queryset = []

    queries = query.split(" ")
    for q in queries:
        news = NewsModel.objects.filter(
                Q(title__icontains=q) |
                Q(body__icontains=q)
            ).distinct()

        for new in news:
            news_queryset.append(new)

    return list(set(news_queryset))