from django.db import models

class Friends(models.Model):
    objects = None
    username = models.TextField(blank=True)
    
    
class song(models.Model):
    
