from django.urls import path
from . import views

urlpatterns = [
    #
    path('', views.listarEvento),
    path('listarEvento/', views.listarEvento),
    path('nuevoEvento/', views.nuevoEvento),
    path('guardarEvento/', views.guardarEvento),
    path('eliminarEvento/<int:id>/', views.eliminarEvento),
    path('editarEvento/<int:id>/', views.editarEvento),
    path('procesarEdicionEvento/', views.procesarEdicionEvento),

    # URLs para Patrocinador
    path('listarPatrocinador/', views.listarPatrocinador),
    path('nuevoPatrocinador/', views.nuevoPatrocinador),
    path('guardarPatrocinador/', views.guardarPatrocinador),
    path('eliminarPatrocinador/<int:id>/', views.eliminarPatrocinador),
    path('editarPatrocinador/<int:id>/', views.editarPatrocinador),
    path('procesarEdicionPatrocinador/', views.procesarEdicionPatrocinador),

    # URLs para EventoPatrocinador
    path('listarEventoPatrocinador/', views.listarEventoPatrocinador),
    path('nuevoEventoPatrocinador/', views.nuevoEventoPatrocinador),
    path('guardarEventoPatrocinador/', views.guardarEventoPatrocinador),
    path('eliminarEventoPatrocinador/<int:id>/', views.eliminarEventoPatrocinador),
    path('editarEventoPatrocinador/<int:id>/', views.editarEventoPatrocinador),
    path('procesarEdicionEventoPatrocinador/', views.procesarEdicionEventoPatrocinador),
]
