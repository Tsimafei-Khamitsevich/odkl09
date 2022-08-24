from django.db import models

# Create your models here.
class FormInput(models.Model):
    inputs = models.JSONField()
