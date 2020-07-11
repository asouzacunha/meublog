from django.urls import path # importar urls
from . import views #importar tudo do views

#criar a listagem de postagem
#lista
urlpatterns = [
    #instanciar a path
    #path('paginainicial', 'views.funcao', referencia para chamar o link: name="home")
    path('', views.home, name="home"),
    path('post/<int:pk>/', views.detalhe_post, name="detalhe_post")


]