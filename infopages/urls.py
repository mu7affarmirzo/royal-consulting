from django.urls import path
from infopages.views import *

app_name = 'infopages'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about')
]