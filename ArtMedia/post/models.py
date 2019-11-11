from django.db import models
from django.contrib.auth.models import User 
from register.models import Profile

# Create your models here.
class Post(models.Model):
    img = models.ImageField(upload_to='posts',verbose_name='Imagen')
    detail = models.TextField(verbose_name='Detalle')
    user = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de publicacion')