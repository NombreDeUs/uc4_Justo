from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    hour = models.IntegerField()
    credits = models.IntegerField()
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.name

from django.db import models

class Career(models.Model):
    name = models.CharField(max_length=100)
    shortname = models.CharField(max_length=20)
    image = models.ImageField(upload_to='careers/')
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.name