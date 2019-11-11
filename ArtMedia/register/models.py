from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

# costom upload
def custom_upload(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profile/' + filename

# modelos
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Nombre de usuario', on_delete=models.CASCADE)
    avatar = models.ImageField(default='profile/perfil_img.jpg', upload_to=custom_upload, null=True, blank=True)
    bio = models.TextField(verbose_name='Biografia')
    link = models.URLField(max_length=200, null=True, blank=True)
    block = models.BooleanField(default=False, verbose_name='Bloquear usuario')

    def __str__(self):
        return str(self.user)
    

@receiver(post_save, sender = User)
def ensuere_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print('Se ha creado un usuario y su perfil enlazado')