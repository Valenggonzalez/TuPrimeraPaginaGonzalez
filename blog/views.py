from django.shortcuts import render
from .forms import AutorForm, PostForm, ComentarioForm, BuscarPostForm
from .models import Post

def inicio(request):
    return render(request, "blog/inicio.html")


def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AutorForm()

    return render(request, "blog/form_autor.html", {"form": form})


def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()

    return render(request, "blog/form_post.html", {"form": form})


def crear_comentario(request):
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ComentarioForm()

    return render(request, "blog/form_comentario.html", {"form": form})


def buscar_post(request):
    resultados = []

    if request.method == "POST":
        form = BuscarPostForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data["titulo"]
            resultados = Post.objects.filter(titulo__icontains=titulo)
    else:
        form = BuscarPostForm()

    return render(request, "blog/buscar.html", {"form": form, "resultados": resultados})