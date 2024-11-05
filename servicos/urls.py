from django.urls import path, include
from . import views

urlpatterns = [
   path('', include('login.urls')),
   path('novo_servico/', views.novo_servico, name="novo_servico"),
   path('listar_servico/', views.listar_servico, name="listar_servico"),
   path('servico/<str:identificador>/', views.servico, name="servico"),
   path('gerar_os/<str:identificador>', views.gerar_os, name="gerar_os"),
   # path('servico_adicional/', views.servico_adicional, name="servico_adicional")
]