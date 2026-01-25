from django.urls import path, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
from . import views

urlpatterns = [
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('', views.home, name='home'),
    path('en/', views.home, {'lang': 'en'}, name='home_en'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('en/kontakt/', views.kontakt, {'lang': 'en'}, name='kontakt_en'),
    path('galeria/', views.galeria, name='galeria'),
    path('en/galeria/', views.galeria, {'lang': 'en'}, name='galeria_en'),
    path('polityka-prywatnosci/', views.privacy_policy, name='privacy_policy'),
    path('en/polityka-prywatnosci/', views.privacy_policy, {'lang': 'en'}, name='privacy_policy_en'),
]

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]