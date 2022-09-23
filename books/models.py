from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Books(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=255, blank=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

