from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('events/', views.events, name='events'),
    path('gallery/', views.gallery, name='gallery'),
    path('load-more-images/', views.load_more_images, name='load_more_images'),
    path('media/', views.media, name='media'),
    path('load-more-media/', views.load_more_media, name='load_more_media'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('contact/', views.contact, name='contact'),
    path('terms_of_use/', views.terms_of_use, name='terms_of_use'),
    path('privacy/', views.privacy_policy, name='privacy'),
    path('help/', views.helps, name='help'),
    path('faq/', views.faq, name='faq'),
    path('career/', views.career, name='career')
    # Add more paths as needed
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)