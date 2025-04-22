from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=140)
    signature = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()
  
    def __str__(self):
        return self.title
