from django.db import models

# Create your models here.
class Cliente(models.Model):
    CI_Cliente = models.ForeignKey(max_length=10, blank=False,primary_key=True)
    Nombre_Cliente = models.CharField(max_length=25, blank=False)
    Apellido_Cliente = models.CharField(max_length=25, blank=False)
    Direccion_Cliente = models.CharField(max_length=50, blank=False)
    Telefono_Cliente = models.CharField(max_length=15, blank=False)
    Email_Cliente = models.EmailField(blank=False)
    Fecha_Nacimiento_Cliente = models.DateField(blank=False)
    Estado_Cliente = models.BooleanField(default=True)
    Observaciones_Cliente = models.TextField(blank=True)
    class Meta:
        verbose_name_plural = 'Clientes'
        ordering = ['CI_Cliente']
        db_table = 'clientes'
    def __str__(self):
    return self.CI_Cliente
