from django.db import models

class Process(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    process_number = models.CharField(max_length=255, unique=True)
    kind = models.TextField()
    area = models.TextField()
    subject = models.TextField()
    distribuition = models.TextField()
    judge = models.TextField()
    action_value = models.TextField()

class Move(models.Model):
    date = models.DateField()
    description = models.TextField()
    process = models.ForeignKey(Process, on_delete=models.CASCADE)

class RelatedPart(models.Model):
    kind = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)

class RelatedPeople(models.Model):
    kind = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    related_part = models.ForeignKey(RelatedPart, on_delete=models.CASCADE)