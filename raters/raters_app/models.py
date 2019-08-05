from django.db import models

# Create your models here.
class raters(models.Model):
    UID=models.CharField(max_length=30)
    age=models.IntegerField()
    location=models.CharField(max_length=20)
    gender=models.IntegerField()
    Workflow=models.IntegerField()

class items(models.Model):
    URL=models.URLField(max_length=50)
    Category=models.CharField(max_length=20)

class workflows(models.Model):
    workflow_name=models.CharField(max_length=50)
    version_number=models.IntegerField()
