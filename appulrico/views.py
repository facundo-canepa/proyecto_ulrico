from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from appulrico.forms import CursoFormulario
from appulrico.forms import ProfesorFormulario
from appulrico.forms import BuscaCursoForm
from appulrico.forms import EstudianteForm
from .forms import ProfesorForm
from .forms import BuscaCursoForm
from appulrico.forms import EstudianteFormulario

from .models import Curso
from .models import Profesor
from .models import Estudiante

# Create your views here.

def index(request):
    return render(request, "appulrico/index.html")

def inicio(request):
    return render(request, "appulrico/inicio.html")

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, "appulrico/cursos.html", {"cursos": cursos})

def estudiantes(request):
    return render(request, "appulrico/estudiantes.html")

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "appulrico/profesores.html", {"profesores": profesores})

def entregables(request):
    return render(request, "appulrico/entregables.html")

def curso_formulario(request):
    if request.method == 'POST':
        curso_formulario = CursoFormulario(request.POST)
        if curso_formulario.is_valid():
            curso = Curso(
                nombre=curso_formulario.cleaned_data['curso'],
                comision=curso_formulario.cleaned_data['comision']
            )
            curso.save()
            return render(request, "appulrico/index.html")
    else:
        curso_formulario = CursoFormulario()
    return render(request, "appulrico/curso_formulario.html", {'curso_formulario': curso_formulario})


def form_con_api(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)  
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
            curso.save()
            return render(request, "appulrico/index.html")
    else:
        mi_formulario = CursoFormulario()
    return render(request, "appulrico/form_con_api.html", {"mi_formulario": mi_formulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        miFormulario = BuscaCursoForm(request.POST) 

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "appulrico/resultados_buscar_form.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()

    return render(request, "appulrico/buscar_form_con_api.html", {"miFormulario": miFormulario})


def profesor_creado_api_form(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'{Profesor.nombre} {Profesor.apellido} se ha creado con éxito!')
            return redirect('index')

    else:
        form = ProfesorForm()
    return render(request, 'appulrico/form_profesor.html', {'form': form})

def profesor2_creado_api_form(request):
    if request.method == 'POST':
        profesor_formulario = ProfesorFormulario(request.POST)
        if profesor_formulario.is_valid():
            profesor = Profesor(
                nombre=profesor_formulario.cleaned_data['nombre'],
                apellido=profesor_formulario.cleaned_data['apellido'],
                email=profesor_formulario.cleaned_data['email'],
                especialidad=profesor_formulario.cleaned_data['especialidad']
            )
            profesor.save()
            messages.success(request, f'{profesor.nombre} {profesor.apellido} se ha creado con éxito!')
            profesor_formulario = ProfesorFormulario() 
        else:
            messages.error(request, 'Error al crear el profesor. Por favor, revisa los datos ingresados.')
    else:
        profesor_formulario = ProfesorFormulario()
    return render(request, "appulrico/profesor_formulario.html", {'profesor_formulario': profesor_formulario})
    
def estudiante_creado_api_form(request):
    if request.method == 'POST':
        estudiante_formulario = EstudianteFormulario(request.POST)
        if estudiante_formulario.is_valid():
            estudiante = Estudiante(
                nombre=estudiante_formulario.cleaned_data["nombre"], 
                apellido=estudiante_formulario.cleaned_data["apellido"],
                dni=estudiante_formulario.cleaned_data["dni"], 
                email=estudiante_formulario.cleaned_data["email"],
                profesion=estudiante_formulario.cleaned_data["profesion"],
            )
            estudiante.save()
            messages.success(request, f'{estudiante.nombre} {estudiante.apellido} se ha creado con éxito!')
            return redirect('index')
        else:
            messages.error(request, 'Error al crear el estudiante. Por favor, revisa los datos ingresados.')
    else:
        estudiante_formulario = EstudianteFormulario()
    return render(request, "appulrico/estudiante_formulario.html", {'estudiante_formulario': estudiante_formulario})


def buscar_curso(request):
    if request.method == 'POST':
        form = BuscaCursoForm(request.POST)
        if form.is_valid():
            nombre_curso = form.cleaned_data['nombre']
            cursos = Curso.objects.filter(nombre__icontains=nombre_curso)
            return render(request, 'appulrico/resultados_buscar_form.html', {'cursos': cursos})
    else:
        form = buscar_curso()
    
    return render(request, 'appulrico/buscar_form_html_con_api.html', {'miFormulario': form})

def success_view(request):
    return render(request, 'appulrico/ingreso_exitoso.html')


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            nombre_usuario = form.save()
            nombre_usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            nombre_usuario = authenticate(nombre_usuario=nombre_usuario, contraseña=contraseña,email=email)
            login(request, nombre_usuario)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'appulrico/registro.html', {'form': form})


def crear_usuario(data):
    nombre_usuario = data.get('username')
    email = data.get('email')
    contraseña = data.get('password1')
    
    user = User.objects.create_user(nombre_usuario=nombre_usuario, email=email, contraseña=contraseña)
    user.save()
    
    return user

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            
            user = authenticate(username = usuario, password = contraseña)
            
            if user is not None:
                login(request, user)
                
                return render(request,"Appulrico/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            
            else: 
                
               return render(request,"Appulrico/inicio.html", {"mensaje":f"Error, datos incorrectos {usuario}"})
           
    form = AuthenticationForm()
           
    return render(request,"appulrico/login.html", {'form':form})
            
    
    