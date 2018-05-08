""" Define padrões de URL para Learning_logs"""

from django.urls import path
from . import views

urlpatterns = [
    # Pagina Inicial
    path('', views.index, name='index'),

    # Mostrando todos os assuntos
    path('topics/', views.topics, name='topics'),

    # Pagina de detalhes para o assunto Topics-Chess.
    path('topics/<topic_id>',  views.topic, name='topic'),

    #Pagina para adicionar um novo assunto
    path('new_topic/', views.new_topic, name='new_topic'),

    # Pagina para adicionar uma nova entrada
    path('new_topic/<topic_id>', views.new_entry, name='new_entry'),

    # Pagina para editar uma entrada
    path('edit_entry/<entry_id>', views.edit_entry, name='edit_entry'),
]