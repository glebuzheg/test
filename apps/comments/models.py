from django.db import models

# Create your models here.
from apps.images.models import Image


class Comment(models.Model):
    text = models.CharField(max_length=64, verbose_name='Comment text')
    image = models.ForeignKey(Image, related_name='comments', verbose_name='Image', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created date')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
