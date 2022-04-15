from unicodedata import name
from django.db import models
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phn_num = models.CharField(max_length=10)
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=500)