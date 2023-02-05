from django.urls import path

from estudiantes.views import (listar_profesores,listar_cursos,listar_estudiantes,about1,
    crear_curso, buscar_cursos, ver_curso, editar_curso, eliminar_curso,
    EstudianteListView, EstudianteCreateView, EstudianteUpdateView,ProfileUpdateView,
    EstudianteDeleteView, EstudianteDetailView,login_request,registro,agregar_avatar,Blog)
    
     
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import  logout, authenticate
from django.contrib.auth.views import LogoutView

from estudiantes.views import (añadir_estudiante,añadir_profesor,login_request)


urlpatterns = [
    path('estudiantes/',listar_estudiantes, name="listar_estudiantes"),
    path('profesores/', listar_profesores, name="listar_profesores"),
    path('crear-curso/', crear_curso, name="crear_curso"),
    path('añadir-estudiante/',añadir_estudiante, name="añadir_estudiante"),
    path('añadir-profesor/',añadir_profesor, name="añadir_profesor"),
    # URLS de cursos (basadas den views funcionales)
    path('cursos/', listar_cursos, name="listar_cursos"),
    path('buscar-cursos/', buscar_cursos, name="buscar_cursos"),
    path('cursos/<int:id>/', ver_curso, name="ver_curso"),
    path('editar-curso/<int:id>/', editar_curso, name="editar_curso"),
    path('eliminar-curso/<int:id>/', eliminar_curso, name="eliminar_curso"),
    # URLS de alumnos (basadas den Class Based Views, vistas basadas en clases)
    path('alumnos/', EstudianteListView.as_view(), name="listar_alumnos"),
    path('alumnos/<int:pk>/', EstudianteDetailView.as_view(), name="ver_alumno"),
    path('crear-alumno/', EstudianteCreateView.as_view(), name="crear_alumno"),
    path('editar-alumno/<int:pk>/', EstudianteUpdateView.as_view(), name="editar_alumno"),
    path('eliminar-alumno/<int:pk>/', EstudianteDeleteView.as_view(), name="eliminar_alumno"),
    path('about1/', about1, name='about1'),
    path('login/', login_request, name="Login"),
    path('register/',registro, name="Registro"),
    path('logout', LogoutView.as_view(template_name='estudiantes/logout.html'), name='Logout'),
    path('editar-Perfil',ProfileUpdateView.as_view(), name="EditarPerfil"),
    path('agregar-avatar/',agregar_avatar, name="Agregar_avatar"),
    path('pages/',Blog,name="pages")
    ]
