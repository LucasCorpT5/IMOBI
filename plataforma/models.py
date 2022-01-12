from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Imagem(models.Model):
    img = models.ImageField(upload_to='img')
