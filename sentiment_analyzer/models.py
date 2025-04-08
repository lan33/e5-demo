from django.db import models

class Analysis(models.Model):
    text = models.TextField()
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
