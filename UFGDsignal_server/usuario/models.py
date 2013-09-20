from django.db import models
from django.contrib.auth.models import User


class AnuncianteProfile(models.Model):
    usuario = models.ForeignKey(User, unique = True)
    cpf = models.CharField(max_length=14,primary_key=True)
    cargo = models.CharField(max_length=15)
    
    def __unicode__(self):
        return self.usuario.username

class AdminProfile(models.Model):
    usuario = models.ForeignKey(User, unique = True)
    cpf = models.CharField(max_length=14,primary_key=True)
    cargo = models.CharField(max_length=15)
    
    def __unicode__(self):
        return self.usuario.username
    
class ConfigProfile(models.Model):
    usuario = models.ForeignKey(User, unique = True)
    cpf = models.CharField(max_length=14,primary_key=True)
    cargo = models.CharField(max_length=15)
    
    def __unicode__(self):
        return self.usuario.username    

    

    
