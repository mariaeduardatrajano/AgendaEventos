from django.shortcuts import render
from .models import Evento, Organizador, Participante, Local
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.db.models import ManyToManyField

def get_field_values(instance): # Pegando os campos dos modelos
  field_values = {}
  fields = instance._meta.get_fields(include_hidden=True)

  for field in fields:
    try:
      if isinstance(field, ManyToManyField):
        related_objects = getattr(instance, field.name).all()
        field_values[field.name] = ', '.join(str(obj) for obj in related_objects)
      else:
        field_values[field.name] = getattr(instance, field.name)
    except Exception:
        pass

  return field_values

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

class evento_detail(DetailView):
  model = Evento
  template_name = 'instancias-detalhes.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)   
    context['object'] = get_field_values(context['object'])
    context['Model'] = 'eventos'
    return context

class organizador_detail(DetailView):
  model = Organizador
  template_name = 'instancias-detalhes.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object'] = get_field_values(context['object'])
    context['Model'] = 'organizadores'
    return context

class participante_detail(DetailView):
  model = Participante
  template_name = 'instancias-detalhes.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object'] = get_field_values(context['object'])
    context['Model'] = 'participantes'
    return context

class local_detail(DetailView):
  model = Local
  template_name = 'instancias-detalhes.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object'] = get_field_values(context['object'])
    context['Model'] = 'locais'
    return context