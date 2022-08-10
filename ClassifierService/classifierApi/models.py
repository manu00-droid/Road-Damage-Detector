from django.db import models

# Create your models here.

from django.core.validators import FileExtensionValidator

# Create your models here.
class picture(models.Model):
    # description = models.TextField()
    pic = models.ImageField(upload_to="userPics/",validators=[FileExtensionValidator( ['png','jpg','jpeg'] ) ])
    