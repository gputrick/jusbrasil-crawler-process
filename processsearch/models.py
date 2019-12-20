from django.db import models

#Move entity
class Move(models.Model):
    date = models.DateField()
    description = models.TextField()

class RelatedPeople(models.Model):
    kind = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

class RelatedPart(models.Model):
    kind = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    related_people = models.ManyToManyField(RelatedPeople)

#Process entity
class Process(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    process_number = models.CharField(max_length=255, unique=True)
    kind = models.TextField()
    area = models.TextField()
    subject = models.TextField()
    distribuition = models.TextField()
    judge = models.TextField()
    action_value = models.TextField()
    #TODO search how to map list oneToMany in django
    moves = models.ManyToManyField(Move)
    related_parts = models.ManyToManyField(RelatedPart)
