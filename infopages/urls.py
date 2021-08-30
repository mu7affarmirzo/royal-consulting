from django.urls import path
from infopages.views import *

app_name = 'infopages'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('news/', news_list_view, name='news-list'),
    path('news/<slug>/', detail_news_view, name="news-detail"),

    # path('coming/', ComingSoonView.as_view(), name='coming'),
    # path('faq/', FaqView.as_view(), name='faq'),
    # path('central-asia/', CentralAsiaView.as_view(), name='central-asia'),
    # path('resources-asia/', RerourcesView.as_view(), name='resources-asia'),
    # path('contact-us/', ContactsView.as_view(), name='contacts'),

    # path('story/<slug>/', individual_view, name="story-detail"),
]