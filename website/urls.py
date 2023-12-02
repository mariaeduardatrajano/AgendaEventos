from django.urls import path
from . import views

urlpatterns = [
  path('', views.index.as_view(), name='index'),
  path('eventos', views.evento_list.as_view(), name='eventos'),
  path('eventos/adicionar', views.evento_add.as_view(), name='adicionar evento'),
  path('organizadores', views.organizador_list.as_view(), name='organizadores'),
  path('organizadores/adicionar', views.organizador_add.as_view(), name='adicionar organizador'),
  path('participantes', views.participante_list.as_view(), name='Participantes'),
  path('participantes/adicionar', views.participante_add.as_view(), name='adicionar participante'),
  path('locais', views.local_list.as_view(), name='locais'),
  path('locais/adicionar', views.local_add.as_view(), name='adicionar local')
]