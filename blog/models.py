from django.db import models

# Create your models here.
from django.utils import timezone
class Post(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True,null=True)
    def publish(self):
        self.published_date=timezone.now()
        self.save()
    def _str_(self):
        return self.title
