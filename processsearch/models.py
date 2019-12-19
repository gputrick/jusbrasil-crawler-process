from django.db import models


class Move(models.Model):
    date = models.DateField()
    description = models.TextField()

class Process(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    process_number = models.CharField(max_length=255, unique=True)
    process = models.TextField()
    classe = models.TextField()
    subject = models.TextField()
    distribuition = models.TextField()
    control = models.TextField()
    judge = models.TextField()
    action_value = models.TextField()
    moves = models.ManyToManyField(Move)
