from enum import unique
from tkinter.messagebox import YES
from unicodedata import decimal
from django.db import models
from django.forms.widgets import Textarea
from rcodec.settings import BASE_DIR

class Repositorio (models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=999)
    titulor = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='upload/pdf', blank=True)

class Tcc (models.Model):
    codigo = models.AutoField(primary_key=True)
    titulot = models.CharField(max_length=800)
    descricao = models.CharField(max_length=999)
    arquivo = models.FileField(upload_to='tcc/pdf', blank=True)