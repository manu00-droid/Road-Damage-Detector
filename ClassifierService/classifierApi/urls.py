from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('classify/', views.imageHandler),
    path('classify/zip/', views.zipHandler),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
