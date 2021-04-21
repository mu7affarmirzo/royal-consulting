from django.shortcuts import render, redirect, get_object_or_404
from operator import attrgetter

from django.db.models import Q

from entrepreneur.models import *

def entrepreneur_view(request, *args, **kwargs):

    industries = IndustriesModel.objects.all()
    businesses = list(BusinessModel.objects.all())[:4]
    filters = FilterModel.objects.all()
    context = {
        'industries': industries,
        'businesses': businesses,
        'filters': filters
    }

    return render(request, "pages/entrepreneur-index.html", context)


def detail_industies_view(request, slug):

    context = {}

    posts = get_object_or_404(IndustriesModel, slug=slug)
    context['posts'] = posts

    return render(request, 'pages/industries_detail.html', context)

def detail_business_view(request, slug):

    context = {}

    posts = get_object_or_404(BusinessModel, slug=slug)
    context['posts'] = posts

    return render(request, 'pages/business_detail.html', context)

def detail_indust_view(request, slug):

    context = {}

    posts = get_object_or_404(IndustriesModel, slug=slug)
    context['posts'] = posts

    return render(request, 'pages/business_detail.html', context)

# def detail_news_view(request, slug):
#
#     context = {}
#
#     posts = get_object_or_404(NewsModel, slug=slug)
#     context['posts'] = posts
#
#     return render(request, 'pages/news_detail.html', context)