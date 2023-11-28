from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    # path('generate_image', views.generate_image, name='generate_image'),
    path('download_image',views.download_image,name = 'download_image'),
    path('auth/', include('social_django.urls', namespace='social')),
    ]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)