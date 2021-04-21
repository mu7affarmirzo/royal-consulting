from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView
from operator import attrgetter

from django.db.models import Q

from investors.models import *
from investors.forms import *

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

def form_view(request, *args, **kwargs):
    context = {}
    return render(request,'pages/investor-form.html', context)

class FormView(View):
    def get(self, *args, **kwargs):
        form = InvestorForm()
        context = {
            'form': form,
        }
        return render(self.request, 'pages/investor-form.html', context)
    def post(self, *args, **kwargs):
        form = InvestorForm(self.request.POST or None)
        if form.is_valid():
            country = form.cleaned_data.get('country')
            full_name = form.cleaned_data.get('full_name')
            company_name = form.cleaned_data.get('company_name')
            postion = form.cleaned_data.get('postion')
            number = form.cleaned_data.get('number')
            email = form.cleaned_data.get('email')
            investment_value = form.cleaned_data.get('investment_value')
            message = form.cleaned_data.get('message')

            user_application = UserApplication(
                country = self.request.country,
                full_name = self.request.full_name,
                company_name = self.request.company_name,
                postion = self.request.postion,
                number = self.request.number,
                email = self.request.email,
                investment_value = self.request.investment_value,
                message = self.request.message,
            )
            user_application.save()
            # if save_info:

            print(form.cleaned_data)
            return redirect('home')
        else:
            print('form invalid')
            return redirect('infopages:about')



def create_applic_view(request):

    context = {}

    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)

        obj.save()
        form = CreateBlogPostForm()
        return redirect('home')

    context['form'] = form

    return render(request, "pages/form.html", context)