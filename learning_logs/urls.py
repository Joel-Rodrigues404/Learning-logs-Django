"""Define padroes de urls para learning logs"""

from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    #Pagina inicial
    path('', views.index, name='index'),
    #mostra todos os assutos
    path('topics/', views.topics, name='topics'),
    #Pagina detalhada para um unico assunto
    path('topics/<int:topic_id>', views.topic, name='topic'),
    #pagina para adicionar um novo assunto
    path('new_topic', views.new_topic, name='new_topic'),
    #pagina para adicionar uma nova entrada
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    #pagina para editar entradas existentes
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]

