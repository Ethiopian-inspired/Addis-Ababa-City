from django.db import models

# Create your models here.

class IndexObjects (models.Model):

    ImgName = models.CharField (max_length=55)
    Image = models.ImageField (upload_to='Index_Image/')

    def __str__(self):
        return self.ImgName