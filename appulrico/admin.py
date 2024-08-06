from django.contrib import admin
from .models import Curso, Estudiante, Profesor, Entregable,Registro

class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "comision")
    list_per_page = 10
    list_filter = ("nombre","comision")
    ordering = ("nombre","comision")
    

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido","dni","profesion", "email")
    list_per_page = 10
    list_filter = ("nombre","apellido")
    ordering = ("apellido","nombre")
    
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email","especialidad")
    list_per_page = 10
    list_filter = ("nombre","apellido")
    ordering = ("apellido","nombre")   

class EntregableAdmin(admin.ModelAdmin):
    list_display = ("nombre", "entregado") 

class RegistroAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email")
    list_per_page = 10
    list_filter = ("nombre", "apellido", "email")
    ordering = ("nombre", "apellido", "email") 
    
    
admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Entregable, EntregableAdmin)
admin.site.register(Registro, RegistroAdmin)
