from django.urls import path
from .import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('media-gallery/', views.media_gallery, name='media_gallery'),
    path('upload-gallery/', views.upload_gallery, name='upload_gallery'),
    path('view-gallery/<int:id>/', views.view_gallery, name='view_gallery'),
    path('view-service/<int:id>/', views.view_service, name='view_service'),
]
