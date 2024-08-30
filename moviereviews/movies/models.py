from django.db import models

# Create your models here.
class Email(models.Model):
    emailId=models.EmailField(max_length=50,unique=True)

    def __str__(self):
        return self.emailId

class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image=models.ImageField(upload_to='movies/images')
    url=models.URLField(blank=True)

    def __str__(self):
        return self.title