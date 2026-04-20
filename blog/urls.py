from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('autor/', views.crear_autor),
    path('post/', views.crear_post),
    path('comentario/', views.crear_comentario),
    path('buscar/', views.buscar_post),
]