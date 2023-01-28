from django import forms


class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=64)
    comision = forms.IntegerField(required=True, max_value=2000)
    fecha_inicio = forms.DateField(required=True, max_value=100)
    descripcion = forms.CharField(required=False, max_length=1000)

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=64)
    comision = forms.IntegerField(required=True, max_value=2000)
    descripcion = forms.CharField(required=False, max_length=1000)


class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=64)
    comision = forms.IntegerField(required=True, max_value=2000)
    descripcion = forms.CharField(required=False, max_length=1000)
