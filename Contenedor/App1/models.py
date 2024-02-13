from django.db import models

# Create your models here.
class Profesion(models.Model):
    nombre=models.CharField(max_length=75, verbose_name="Nombre")

    def __str__(self):
        return self.nombre
    
class AutorDb(models.Model):
    # max_length: Límite de caracteres (TODO CUENTA)
    # verbose_name: Como aparece en el admin
    # null: Si aceptamos o no valores nulos
    # blank: Si aceptamos o no valores en blanco
    # ManyToManyField: Relación muchos a muchos
    nombre = models.CharField(max_length=75, verbose_name="Nombre")
    fecha_nacimiento = models.DateField(verbose_name="Fecha Nacimiento", null=False, blank=False)
    fecha_fallecimiento = models.DateField(verbose_name="Fecha Fallecimiento", null=True, blank=True)
    profesion = models.ManyToManyField(Profesion, verbose_name="Profesion", related_name='autores')
    nacionalidad = models.CharField(verbose_name="Nacionalidad", max_length=50)

    # Con meta personalizamos nuestra tabla
    class Meta:
        db_table = "Autores"
        verbose_name = "Autor" # Indicamos como se mostrara en el admin
        verbose_name_plural = "Autores" # Indicamos como se mostrará en plural en el admin

    # Devolvemos un str para presentar la petición
    def __str__(self) -> str:
        return self.nombre

class FraseDb(models.Model):
    cita = models.TextField(verbose_name="Cita", max_length=400)
    autor_fk = models.ForeignKey(AutorDb, on_delete=models.CASCADE, related_name='frases')

    class Meta:
        verbose_name = "Frase"
        verbose_name_plural = "Frases"

    def __str__(self):
        return self.cita
    
