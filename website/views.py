from django.shortcuts import render
from .models import Evento, Organizador, Participante, Local
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView

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

class evento_add(CreateView):
  model = Evento
  fields = ['nome', 'data_hora', 'organizadores', 'participantes', 'local','descricao']
  template_name = 'form.html'
  success_url = '/agenda/eventos'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Adicionando Evento'
    return context
  
class organizador_add(CreateView):
  model = Organizador
  fields = ['nome', 'idade']
  template_name = 'form.html'
  success_url = '/agenda/organizadores'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Adicionando Organizador'
    return context

class participante_add(CreateView):
  model = Participante
  fields = ['nome', 'idade']
  template_name = 'form.html'
  success_url = '/agenda/participantes'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Adicionando Participante'
    return context
  
class local_add(CreateView):
  model = Local
  fields = ['nome', 'endereco', 'capacidade']
  template_name = 'form.html'
  success_url = '/agenda/locais'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Adicionando Local'
    return context
