# tarea_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TareaViewSet
from .views import TareaListCreateView, TareaDetailView, lista_tareas, detalles_tareas 
from . import views

router = DefaultRouter()
router.register(r'tareas', TareaViewSet, basename='tarea')

urlpatterns = [
    path('api/tareas/', TareaListCreateView.as_view(), name='tarea-list-create'),
    path('api/tareas/<int:pk>/', TareaDetailView.as_view(), name='tarea-detail'),
    path('tareas/', lista_tareas, name='tarea-lista'),
    path('tareas/<int:pk>/', detalles_tareas, name='tarea-detalles-template'),
    path('tareas/completada/', views.marcar_completadas, name='tareas-completadas'),
    path('tarea/completada/<int:id_tarea>/', views.marcar_completada, name='tarea-completada'),

]