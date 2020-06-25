from django.db import models


class RawImage(models.Model):
    image_name = models.CharField(max_length=120)
    image_path = models.ImageField(verbose_name='Путь к картинке', upload_to='source_images')

    def __str__(self):
        return self.image_name
