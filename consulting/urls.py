from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

from infopages.views import *

urlpatterns = [
    path('', home_screen_view, name='home'),
    path('about/', AboutView.as_view(), name='about'),

    path('info/', include('infopages.urls', 'staticpages')),
    path('entrepreneur/', include('entrepreneur.urls', 'entrepreneur')),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(

    path('info/', include('infopages.urls')),
    path('entrepreneur/', include('entrepreneur.urls')),
    # path('', include('infopages.urls')),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)