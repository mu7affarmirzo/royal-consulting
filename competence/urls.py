from django.urls import path
from competence.views import *

app_name = 'competence'

urlpatterns = [
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('contact-us/', contact_us_view, name="contact-us"),
    path('<slug>/', details_page_view, name="competence-detail"),
]
