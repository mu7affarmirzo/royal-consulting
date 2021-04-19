from django.urls import path
from infopages.views import *

app_name = 'infopages'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('news/', news_list_view, name='news-list'),
    path('news/<slug>/', detail_news_view, name="news-detail"),
]