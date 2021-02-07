from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=400)
    beginning = models.DateTimeField()
    ending = models.DateTimeField()