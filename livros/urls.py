from django.urls import path
from .views import *

urlpatterns = [

    path('', login_page, name='login_page'),

    path('home/', home, name='home'),

    path('admin-login/',
         admin_login,
         name='admin_login'),

    path('novo/',
         criar_livro,
         name='criar_livro'),

    path('editar/<int:id>/',
         editar_livro,
         name='editar_livro'),

    path('excluir/<int:id>/',
         excluir_livro,
         name='excluir_livro'),

    path('autor/novo/',
         criar_autor,
         name='criar_autor'),

    path('categoria/nova/',
         criar_categoria,
         name='criar_categoria'),
    path('logout/',
     logout_view,
     name='logout'),
]