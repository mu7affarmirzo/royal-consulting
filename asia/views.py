from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def details_page_view(request, slug):

    context = {}
    pages = CentralAsiaPagesModel.objects.all()

    posts = get_object_or_404(CentralAsiaPagesModel, slug=slug)
    # context['posts','pages'] = posts, pages
    context['posts'] = posts
    context['pages'] = pages

    return render(request, 'central-asia.html', context)

