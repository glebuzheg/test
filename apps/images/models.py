from django.db import models
from django.urls import reverse


class Image(models.Model):
    name = models.CharField(max_length=32, verbose_name='Name', blank=True)
    image = models.ImageField(upload_to='images/', verbose_name='Image')
    created_at = models.DateTimeField(verbose_name='Created date', auto_now_add=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def get_absolute_url(self):
        return reverse('image_detail', args=(self.id,))

    def __str__(self):
        return self.name
