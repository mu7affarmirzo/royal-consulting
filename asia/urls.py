from django.urls import path
from asia.views import *

app_name = 'asia'

urlpatterns = [
    path('<slug>/', details_page_view, name="central-asia-detail"),
    # path('<slug>/', details_page_view, name="wedo-detail"),
    # path('opp/<slug>/', details_wedo_page_view, name="opportunities-detail"),
    # path('photo/', photo_bank_view, name="photo"),
]
