from django.urls import path
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos/', views.cursos, name='cursos'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('profesores/', views.profesores, name='profesores'),
    path('entregables/', views.entregables, name='entregables'),
    path('curso-formulario/', views.curso_formulario, name='curso_formulario'),
    path('form-con-api/', views.form_con_api, name='form_con_api'),
    path('buscar-form-con-api/', views.buscar_form_con_api, name='buscar_form_con_api'),
    path('estudiante_creado_api_form/', views.estudiante_creado_api_form, name='estudiante_creado_api_form'),
    path('profesores-create-api-form/', views.profesor_creado_api_form, name='form_profesor'),
    path('profesor2_creado_api_form/', views.profesor2_creado_api_form, name='profesor2_creado_api_form'),
    path('ingreso_exitoso/', views.success_view, name='ingreso_exitoso'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_request, name='login'),
    path('iniciar-sesion/', views.login_request, name='iniciar_sesion'),
    path('cerrar-sesion/', auth_views.LogoutView.as_view(), name='cerrar_sesion'),
    path('index/', views.index, name='index'), 
]
