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
