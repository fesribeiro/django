from django.db import models

# Create your models here.

<<<<<<< HEAD
class Perfil(models.Model):    
=======
class Perfil(models.Model):
>>>>>>> 92ee4bb4f8fd41de2fbe3383fdb8ab1bfef73206
    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)
<<<<<<< HEAD

=======
    
    
>>>>>>> 92ee4bb4f8fd41de2fbe3383fdb8ab1bfef73206
