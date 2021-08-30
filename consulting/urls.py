from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

from infopages.views import *

admin.site.site_header = "Royal Consulting Admin"
admin.site.site_title = "Royal Consulting Admin Portal"
admin.site.index_title = "Welcome to Royal Consulting official web-site!"

urlpatterns = [
    path('', home_screen_view, name='home'),
    # path('home/', home_screen_view, name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('info/', include('infopages.urls', 'staticpages')),

    path('wedo/', include('wedo.urls', 'wedo')),
    path('central-asia/', include('asia.urls', 'asia')),
    path('competence/', include('competence.urls', 'competence')),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(

    path('info/', include('infopages.urls')),
    path('wedo/', include('wedo.urls')),
    path('central-asia/', include('asia.urls')),
    path('competence/', include('competence.urls')),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)