from django.urls import path
from . import views

urlpatterns = [
  path('', views.index.as_view(), name='index'),
  path('eventos', views.evento_list.as_view(), name='eventos'),
  path('organizadores', views.organizador_list.as_view(), name='organizadores'),
  path('participantes', views.participante_list.as_view(), name='Participantes'),
  path('locais', views.local_list.as_view(), name='locais')
]