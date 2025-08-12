from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class Pet(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    pet_image = CloudinaryField('image',null=True)

class Books(models.Model):
    title = models.TextField(max_length=100)
    author = models.CharField(max_length=20)
    published_date = models.DateField()

    def __str__(self):
        return self.title