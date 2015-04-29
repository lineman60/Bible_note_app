from django.db import models

# Create your models here.
class KJV_Bible(models.Model):
    kjv_book = models.CharField(max_length=60)
    kjv_chapter = models.IntegerField()
    kjv_verse = models.IntegerField()
    kjv_verse_text = models.TextField(max_length=400)