from django.shortcuts import render
from .models import Evento, Organizador, Participante, Local
from django.views import View
from django.views.generic import ListView

class index(View):
  def get(self, request):
    return render(request, 'index.html')

class evento_list(ListView):
  model = Evento

  def get(self, request):
    return render(request, 'listar-instancias.html', {'objects': Evento.objects.all(), 'Model': 'eventos'})

class organizador_list(ListView):
  model = Organizador

  def get(self, request):
    return render(request, 'listar-instancias.html', {'objects': Organizador.objects.all(), 'Model': 'organizadores'})

class participante_list(ListView):
  model = Participante

  def get(self, request):
    return render(request, 'listar-instancias.html', {'objects': Participante.objects.all(), 'Model': 'participantes'})

class local_list(ListView):
  model = Local

  def get(self, request):
    return render(request, 'listar-instancias.html', {'objects': Local.objects.all(), 'Model': 'locais'})