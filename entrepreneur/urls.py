from django.urls import path
from entrepreneur.views import *

app_name = 'entrepreneur'

urlpatterns = [
    path('', entrepreneur_view, name='entrepreneur'),
    path('<slug>/', detail_industies_view, name='detailed-industies'),
    # path('news/', news_list_view, name='news-list'),
    # path('news/<slug>/', detail_news_view, name="news-detail"),
]