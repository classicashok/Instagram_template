from django.db import models

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.TextField(max_length=255)
    photo =models.ImageField(upload_to='profile_pic')

    def __str__(self):
        return self.username
