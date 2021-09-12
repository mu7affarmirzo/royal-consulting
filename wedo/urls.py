from django.urls import path
from wedo.views import *

app_name = 'wedo'

urlpatterns = [
    path('news-list/', news_list_view, name="news-list"),
    path('news-list/<slug>', news_detial_view, name="news-detail"),
    path('photo/', photo_bank_view, name="photo"),
    path('facts/', interesting_facts_page_view, name="facts"),
    path('statistics/', statistics_page_view, name="statistics"),
    path('publications/', statistics_page_view, name="publications"),
    path('<slug>/', details_page_view, name="wedo-detail"),
    path('opp/<slug>/', details_wedo_page_view, name="opportunities-detail"),
    # path('news-list/', news_list_view, name="news-list"),
    # path('photo/', photo_bank_view, name="photo"),
]
