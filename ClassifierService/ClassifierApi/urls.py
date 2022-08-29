from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('classify/', views.imageHandler),
    path('classify/zip/', views.zipHandler),
    path('addpoints/', views.addpoint   ),
    path('getpoints', views.getPoints),
    path('zipwcsv',views.zipHandlerwCSV),
    path('login/',views.login),
    path('signup/',views.signup),
    path('displayAll',views.displayAllProjects),
    path('selectProj',views.displaySelectProjects),
    path('addProj',views.addProj),
    path('updateProj',views.updateProj),
    path('getTypeFromEmail',views.getTypeFromEmail),
    path('thingToClient',views.thingToClient),


]