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
    Instruction=models.CharField(max_length=100,default='Default Instruction')
    Judgement_question=models.CharField(max_length=100,default='Model Judgement question')
    Prediction_question=models.CharField(max_length=100,default='Model Prediction question')

class answers(models.Model):
    rater_id=models.CharField(max_length=30)
    item_id=models.CharField(max_length=30)
    workflow_id=models.CharField(max_length=30)
    start_time=models.DateTimeField(auto_now_add=True)
    submit_time=models.DateTimeField(auto_now_add=True)
    Judmenent_answer=models.CharField(max_length=100,blank=True)
    Prediction_A=models.CharField(max_length=100,blank=True)
    Prediction_B=models.CharField(max_length=100,blank=True)
    Prediction_C=models.CharField(max_length=100,blank=True)

