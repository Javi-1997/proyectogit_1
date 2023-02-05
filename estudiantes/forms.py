from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,AbstractUser

from estudiantes.models import Profesor, Avatar,Entrada_de_blog

class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=64)
    comision = forms.IntegerField(required=True, max_value=2000)
    fecha_inicio = forms.DateField(required=True)
    descripcion = forms.CharField(required=False, max_length=1000)

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=64)
    comision = forms.IntegerField(required=True, max_value=2000)
    descripcion = forms.CharField(required=False, max_length=1000)


class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=64)
    comision = forms.IntegerField(required=True, max_value=2000)
    descripcion = forms.CharField(required=False, max_length=1000)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','last_name','first_name']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']


class UserUpdateForm(forms.ModelForm):
    
    email= forms.EmailField(label='mail')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']

class BlogFormulario(forms.ModelForm):
    cuerpo = forms.CharField(max_length=1000, widget=forms.Textarea())
    fecha_publicacion = forms.DateField(required=True)

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        super(BlogFormulario, self).__init__(*args, **kwargs)
        self.fields['usuario'].widget = HiddenInput()

    class Meta:
        model = Entrada_de_blog
        fields = ['usuario','titulo','subtitulo','cuerpo','fecha_publicacion','autor','imagen']



class EditNoticiasForm(forms.ModelForm):
    cuerpo = forms.CharField(max_length=1000, widget=forms.Textarea())
    fecha_publicacion = forms.DateField(required=True)

    class Meta:
        model = Entrada_de_blog
        fields = ['titulo','subtitulo','cuerpo','fecha_publicacion','autor','imagen']