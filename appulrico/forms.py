from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CursoFormulario(forms.Form):
    curso = forms.CharField()
    comision = forms.IntegerField()

class BuscaCursoForm(forms.Form):
    nombre_curso = forms.CharField(max_length=100)
    comision = forms.IntegerField()


class BuscaCursoForm(forms.Form):
    curso = forms.CharField()

class BuscaEstudianteForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()

class EstudianteForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()
    

class ProfesorForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    profesion = forms.CharField()
    email = forms.EmailField()


class EntregableFormulario(forms.Form):
    nombre = forms.CharField()
    fecha_entrega = forms.DateField(widget=forms.SelectDateWidget)
    entregado = forms.BooleanField(required=False)
    
class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    especialidad = forms.CharField()
    email = forms.EmailField()
    
class EstudianteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    edad = forms.IntegerField()
    email = forms.EmailField()
    profesion = forms.CharField()
   
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class CrearUsuario:
        model = User
        informacion = ['nombre', 'email', 'contraseña1', 'contraseña2']