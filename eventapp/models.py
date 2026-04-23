from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    location = models.CharField(max_length = 100)
    datetime = models.DateTimeField()
    image = models.ImageField()
    

    def __str__(self):
        return self.title
