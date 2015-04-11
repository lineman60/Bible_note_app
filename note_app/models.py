from django.db import models

# Create your models here.

class Anote(models.Model):
    book = models.CharField(max_length=60)
    chapter = models.IntegerField()
    verse = models.IntegerField()
    note_text = models.TextField(max_length=400)
    note_source = models.CharField(max_length=60)
    is_public = models.BooleanField(default=False)
    contributor = models.CharField(max_length=128)
