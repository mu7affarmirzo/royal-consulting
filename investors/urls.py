from django.urls import path
from investors.views import *

app_name = 'investor'

urlpatterns = [
    path('', investor_view, name='investor-index'),
    path('<slug>/', detail_industies_view, name='detailed-industies'),
    # path('news/', news_list_view, name='news-list'),
    # path('news/<slug>/', detail_news_view, name="news-detail"),
]