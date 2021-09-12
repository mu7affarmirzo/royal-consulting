from django.shortcuts import render, redirect, get_object_or_404
from competence.models import *
from django.views.generic import TemplateView
from competence.forms import ContactUsForm



def details_page_view(request, slug):

    context = {}
    pages = CompetenceModel.objects.all()


    posts = get_object_or_404(CompetenceModel, slug=slug)
    blocks = posts.blocks.all()
    # context['posts','pages'] = posts, pages
    context['posts'] = posts
    context['pages'] = pages
    context['blocks'] = blocks

    return render(request, 'competence.html', context)


class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'


def contact_us_view(request):

    context = {}

    form = ContactUsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)

        obj.save()
        form = ContactUsForm()
        return redirect('home')

    context['form'] = form

    return render(request, "contact.html", context)
