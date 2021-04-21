from django.urls import path
from investors.views import *

app_name = 'investor'

urlpatterns = [
    path('', investor_view, name='investor-index'),
    # path('form/', FormView.as_view(), name='investor-form'),
    path('form/', create_applic_view, name='form'),
    path('<slug>/', detail_industies_view, name='detailed-industies'),
]