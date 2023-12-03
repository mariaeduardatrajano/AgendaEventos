from django.urls import path
from . import views

urlpatterns = [
  path('participantes/detalhes/<int:pk>', views.participante_detail.as_view(), name='detalhes participante'),
  path('organizadores/detalhes/<int:pk>', views.organizador_detail.as_view(), name='detalhes organizador'),
  path('participantes/editar/<int:pk>', views.participante_update.as_view(), name='editar participante'),
  path('organizadores/deletar/<int:pk>', views.organizdaor_delete.as_view(), name='deletar organizador'),
  path('participantes/deletar/<int:pk>', views.participante_delete.as_view(), name='deletar participante'),
  path('organizadores/editar/<int:pk>', views.organizador_update.as_view(), name='editar organizador'),
  path('participantes/adicionar', views.participante_add.as_view(), name='adicionar participante'),
  path('organizadores/adicionar', views.organizador_add.as_view(), name='adicionar organizador'),
  path('eventos/detalhes/<int:pk>', views.evento_detail.as_view(), name='detalhes evento'),
  path('eventos/deletar/<int:pk>', views.evento_delete.as_view(), name='deletar evento'),
  path('eventos/editar/<int:pk>', views.evento_update.as_view(), name='editar evento'),
  path('locais/detalhes/<int:pk>', views.local_detail.as_view(), name='detalhe local'),
  path('locais/deletar/<int:pk>', views.local_delete.as_view(), name='deletar local'),
  path('locais/editar/<int:pk>', views.local_update.as_view(), name='editar local'),
  path('eventos/adicionar', views.evento_add.as_view(), name='adicionar evento'),
  path('participantes', views.participante_list.as_view(), name='Participantes'),
  path('organizadores', views.organizador_list.as_view(), name='organizadores'),
  path('locais/adicionar', views.local_add.as_view(), name='adicionar local'),
  path('eventos', views.evento_list.as_view(), name='eventos'),
  path('locais', views.local_list.as_view(), name='locais'),
  path('', views.index.as_view(), name='index'),
]