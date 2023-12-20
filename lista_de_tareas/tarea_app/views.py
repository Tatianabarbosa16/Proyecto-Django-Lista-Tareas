from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import action 
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics, permissions
from .serializers import TareaSerializer
from .models import Tarea

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    @action(detail=False, methods=['GET'])
    def obtener_tareas_limpieza(self):
        tareas_limpieza = Tarea.objects.filter(nombre="Limpieza")
        serializer = self.get_serializer(tareas_limpieza, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['POST'])
    @csrf_protect 
    def crear_tarea_personalizada(self, request):
        # Asumiendo que los datos de la nueva tarea se envían en el cuerpo de la solicitud.
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # 201 Created
        else:
            return Response(serializer.errors, status=400)  # 400 Bad Request
        
     
class TareaListCreateView(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]  
    
    
class TareaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]  

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas_lista.html', {'tareas': tareas}) 

def detalles_tareas(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    return render(request, 'tareas_detalle.html', {'tarea': tarea}) 

def marcar_completada(request, id_tarea):
    tarea = Tarea.objects.filter(id=id_tarea, completada=True)
    return render(request, 'tarea_completada.html', {'tarea': tarea}) 

def marcar_completadas(request):
    tareas = Tarea.objects.filter(completada=True)
    return render(request, 'tarea_completada.html', {'tareas': tareas}) 