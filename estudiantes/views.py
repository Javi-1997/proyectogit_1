from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from estudiantes.models import Estudiante, Profesor, Curso
from estudiantes.forms import CursoFormulario,UserRegisterForm
from estudiantes.forms import EstudianteFormulario,ProfesorFormulario

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from estudiantes.forms import CursoFormulario, ProfesorFormulario, UserRegisterForm, UserEditForm,AvatarFormulario,UserUpdateForm
from django.contrib.auth.models import User

def inicio(request):
    return render(
        request=request,
        template_name='estudiantes/inicio.html',
    )


# def listar_estudiantes(request):
#     ## Aqui iria la validacion del permiso lectura estudiantes
#     contexto = {
#         'estudiantes': Estudiante.objects.all()
#     }
#     return render(
#         request=request,
#         template_name='estudiantes/lista_estudiantes.html',
#         context=contexto,
#     )


def listar_profesores(request):
    contexto = {
        'profesores': Profesor.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_profesores.html',
        context=contexto,
    )

@login_required
def listar_cursos(request):
    contexto = {
        'cursos': Curso.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_cursos.html',
        context=contexto,
    )

def listar_estudiantes(request):
    contexto = {
        'cursos': Estudiante.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_estudiantes.html',
        context=contexto,
    )


def ver_curso(request, id):
    curso = Curso.objects.get(id=id)
    contexto = {
        'curso': curso
    }
    return render(
        request=request,
        template_name='estudiantes/detalle_curso.html',
        context=contexto,
    )


def crear_curso_version_1(request):
    """No la estamos usando"""
    if request.method == "POST":
        data = request.POST
        curso = Curso(nombre=data['nombre'], comision=data['comision'])
        curso.save()
        url_exitosa = reverse('listar_cursos')
        return redirect(url_exitosa)
    else:  # GET
        return render(
            request=request,
            template_name='estudiantes/formulario_curso_a_mano.html',
        )


def crear_curso(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Curso(nombre=data['nombre'], comision=data['comision'], descripcion=data['descripcion'])
            curso.save()
            url_exitosa = reverse('listar_cursos')
            return redirect(url_exitosa)
    else:  # GET
        formulario = CursoFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_curso.html',
        context={'formulario': formulario},
    )


def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso.nombre = data['nombre']
            curso.comision = data['comision']
            curso.descripcion = data['descripcion']
            curso.save()
            url_exitosa = reverse('listar_cursos')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'nombre': curso.nombre,
            'comision': curso.comision,
            'descripcion': curso.descripcion,
        }
        formulario = CursoFormulario(initial=inicial)
    return render(
        request=request,
        template_name='estudiantes/formulario_curso.html',
        context={'formulario': formulario, 'curso': curso, 'es_update': True},
    )


def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        curso.delete()
        url_exitosa = reverse('listar_cursos')
        return redirect(url_exitosa)


def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        cursos = Curso.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(comision__exact=data['busqueda'])
        )
        contexto = {
            'cursos': cursos
        }
        return render(
            request=request,
            template_name='estudiantes/lista_cursos.html',
            context=contexto,
        )


class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'estudiantes/lista_estudiantes.html'


class EstudianteCreateView(CreateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'dni', 'email']
    success_url = reverse_lazy('listar_alumnos')


class EstudianteDetailView(DetailView):
    model = Estudiante
    success_url = reverse_lazy('listar_alumnos')


class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'dni', 'email']
    success_url = reverse_lazy('listar_alumnos')


class EstudianteDeleteView(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('listar_alumnos')


def añadir_estudiante(request):
     if request.method == "POST":
        pass
     else:    
          return render(
              request=request,
              template_name='estudiantes/formulario_estudiantes.html'
        )

def añadir_profesor(request):
     if request.method == "POST":
        pass
     else: #Get   
          return render(
              request=request,
              template_name='estudiantes/formulario_profesores.html'
        )
def about1(request):
    return render(
        request=request,
        template_name='estudiantes/About1.html',
    )

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "estudiantes/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "estudiantes/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "estudiantes/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "estudiantes/login.html", {"form": form})


def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  # Esto lo puedo usar porque es un model form
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='estudiantes/register.html',
        context={'form': formulario},
    )

class listar_cursos (LoginRequiredMixin):
    d=1

@login_required
def incio(request):

    return render(request,"estudiante/listar_estudiantes.html")    

@login_required
def listar_profesores(request):
    contexto = {
        'profesores': Profesor.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_profesores.html',
        context=contexto,
    )

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'estudiantes/formulario_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user



def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES) # Aquí me llega toda la info del formulario html

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = AvatarFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_avatar.html',
        context={'form': formulario},
    )
