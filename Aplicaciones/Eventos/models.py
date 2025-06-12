from django.db import models

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    fecha = models.DateField()
    descripcion = models.TextField()
    foto_evento = models.FileField(upload_to='eventos/fotos', null=True, blank=True)
    pdf_programa = models.FileField(upload_to='eventos/programas', null=True, blank=True)

class Patrocinador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    industria = models.CharField(max_length=200)
    logo_patrocinador = models.FileField(upload_to='patrocinadores/logos', null=True, blank=True)

class EventoPatrocinador(models.Model):
    id = models.AutoField(primary_key=True)
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE)
    patrocinador = models.ForeignKey('Patrocinador', on_delete=models.CASCADE)
    aporte_economico = models.DecimalField(max_digits=15, decimal_places=2)
    pdf_contrato = models.FileField(upload_to='eventos/contratos', null=True, blank=True)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
