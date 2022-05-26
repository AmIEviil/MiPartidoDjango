from django.db import models

from embed_video.fields import EmbedVideoField
# Create your models here.

class Video(models.Model):
    cancha = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self) :
        return str(self.cancha)

    class Meta:
        ordering = ['-fecha']