from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm
from .models import Livro, Autor, Categoria
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# =========================
# LOGIN
# =========================


def login_page(request):

    return render(request,
                  'livros/login.html')


def admin_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request,
                  'livros/admin_login.html')

def home(request):
    livros = Livro.objects.all()

    return render(request, 'livros/home.html', {
        'livros': livros
    })

@login_required
def criar_livro(request):

    form = LivroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'livros/form.html', {
        'form': form
    })

@login_required
def editar_livro(request, id):

    livro = get_object_or_404(Livro, id=id)

    form = LivroForm(
        request.POST or None,
        instance=livro
    )

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'livros/form.html', {
        'form': form
    })

@login_required
def excluir_livro(request, id):

    livro = get_object_or_404(Livro, id=id)

    livro.delete()

    return redirect('home')
# =========================
# FORMS
# =========================

class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor
        fields = '__all__'


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'


# =========================
# AUTOR
# =========================
@login_required
def criar_autor(request):

    form = AutorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'livros/form_generico.html', {
        'form': form,
        'titulo': 'Cadastrar Autor'
    })


# =========================
# CATEGORIA
# =========================
@login_required
def criar_categoria(request):

    form = CategoriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'livros/form_generico.html', {
        'form': form,
        'titulo': 'Cadastrar Categoria'
    })
def logout_view(request):

    logout(request)

    return redirect('login_page')