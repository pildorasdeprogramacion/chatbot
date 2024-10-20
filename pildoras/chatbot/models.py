from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Mensaje(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

class Ticket(models.Model):
    mensaje = models.OneToOneField(Mensaje, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=[('abierto', 'Abierto'), ('cerrado', 'Cerrado')], default='abierto')
    fecha_creacion = models.DateTimeField(auto_now_add=True)