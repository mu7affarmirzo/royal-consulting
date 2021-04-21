from django.shortcuts import render, redirect, get_object_or_404
from operator import attrgetter

from django.db.models import Q

from investors.models import *

def investor_view(request, *args, **kwargs):

    industries = IndustriesModel.objects.all()
    businesses = list(BusinessModel.objects.all())[:4]
    filters = FilterModel.objects.all()
    context = {
        'industies': industries,
        'businesses': businesses,
        'filters': filters
    }

    return render(request, "pages/investor-index.html", context)


def detail_industies_view(request, slug):

    context = {}

    industries = get_object_or_404(IndustriesModel, slug=slug)
    context['industries'] = industries

    return render(request, 'pages/industries_detail.html', context)