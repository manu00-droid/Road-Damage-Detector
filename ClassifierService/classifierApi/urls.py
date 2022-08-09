from django.urls import path
from . import views

urlpatterns = [
    path('classify/', views.imageHandler),
    path('classify/zip/', views.zipHandler),
]
