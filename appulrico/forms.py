from django import forms


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

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()

class ProfesorForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    profesion = forms.CharField()

class EntregableFormulario(forms.Form):
    nombre = forms.CharField()
    fecha_entrega = forms.DateField(widget=forms.SelectDateWidget)
    entregado = forms.BooleanField(required=False)