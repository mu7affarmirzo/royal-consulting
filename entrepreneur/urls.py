from django.urls import path
from entrepreneur.views import *

app_name = 'entrepreneur'

urlpatterns = [
    path('', entrepreneur_view, name='entrepreneur-index'),
    path('industries/<slug>/', detail_indust_view, name='indust'),
    path('business/<slug>/', detail_business_view, name='detailed-business'),
]