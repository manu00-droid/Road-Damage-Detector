from django.db import models

# Create your models here.

from django.core.validators import FileExtensionValidator


class picture(models.Model):

    pic = models.ImageField(upload_to="userPics/",validators=[FileExtensionValidator( ['png','jpg','jpeg'] ) ])

class zipFile(models.Model):
    zip=models.FileField(upload_to="userZip/",validators=[FileExtensionValidator( ['zip'] ) ])
    