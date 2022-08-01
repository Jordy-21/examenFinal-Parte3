from django.db import models

# Create your models here.


class Course(models.Model):
    code = models.TextField(max_length=8)
    name = models.TextField()
    hour = models.TextField()
    credits = models.TextField()
    state = models.CharField(max_length=1)
  