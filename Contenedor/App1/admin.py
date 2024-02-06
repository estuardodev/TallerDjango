from django.contrib import admin
from .models import AutorDb, FraseDb,Profesion
# Register your models here.

# Personalizar un poco los títulos de nuestro admin
admin.site.site_header = "Taller"
admin.site.index_title = "Django"
admin.site.site_title = "Taller"

@admin.register(Profesion) # Registramos la clase ProfesionAdmin que utiliza Profesion
class ProfesionAdmin(admin.ModelAdmin):
    list_display= ["nombre"]
    fields = ["nombre"]

# Creamos un subformulario
class FraseInLine(admin.TabularInline):
    model = FraseDb
    extra = 1

# Creamos el formulario de Autor en el administrador
class AutorAdmin(admin.ModelAdmin):
    fields = ["nombre", "fecha_nacimiento", "fecha_fallecimiento", "profesion", "nacionalidad"]
    list_display = ["nombre", "fecha_nacimiento"]

    inlines = [FraseInLine] # Indicamos que subformulario utilizaremos

    # Creamos nuestra propia acción
    def actualizar_o(self, request, queryset):
        for obj in queryset:
            if "O" in obj.nombre:
                nombre1 = obj.nombre
                obj.nombre = nombre1.replace("O", "o")
                obj.save()

        self.message_user(request, "Exitosamente")
    
    # Le establecemos un mejor nombre
    actualizar_o.short_description = "Actualizar letras O"

    # Agregamos nuestra acción a django
    actions = ["actualizar_o"]

admin.site.register(AutorDb, AutorAdmin) # Otra forma para registrar al admin

@admin.register(FraseDb)
class FraseAdmin(admin.ModelAdmin):
    fields = ["cita", "autor_fk"]
    list_display = ["cita"]