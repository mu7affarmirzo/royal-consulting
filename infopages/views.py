from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class HomeScreenView(TemplateView):
    template_name = 'pages/index.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'


def home_screen_view(request, *args, **kwargs):

    # obj = CarouselModel.objects.all()
    # news = list(NewsModel.objects.all())[:6]
    # menu = MenuModel.objects.all()
    # context = {
    #     'obj': obj,
    #     'menu': menu,
    #     'news': news
    # }
    context = {}

    return render(request, "pages/index.html", context)


def home_screen_view(request, *args, **kwargs):

    industries = IndustriesModel.objects.all()
    # news = list(NewsModel.objects.all())[:6]
    # menu = MenuModel.objects.all()
    context = {
        'industies': industries,
        # 'menu': menu,
    #     'news': news
    }
    # context = {}

    return render(request, "pages/index.html", context)