from django.db import models
import random

TYPE_CHOICES=(
    ("TYPE", "TYPE"),
    ("BLOOD", "BLOOD"),
    ("BREAST", "BREAST"),
    ("LUNG", "LUNG"),
    ("PROSTATE", "PROSTATE"),
    ("SKIN", "SKIN"),
)
GENDER_CHOICES=(
    ("SELECT", "SELECT"),
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE"),
)
STAGE_CHOICES=(
    ("STAGE", "STAGE"),
    ("EARLY", "EARLY"),
    ("ADVANCED", "ADVANCED"),
)
# Create your models here.
class clinic(models.Model):
    cid = models.IntegerField(primary_key=True,unique=True)
    cname = models.CharField(max_length=30)
    cemail=models.EmailField(max_length=40)
    def __str__(self):
        return self.name
    
   
class t(models.Model):
    email=models.EmailField(max_length=40,unique=True)
    def __str__(self):
        return self.email
    
class k(models.Model):
    email=models.EmailField(max_length=40,unique=True)
    type=models.ForeignKey(t,on_delete=models.CASCADE)
    def __str__(self):
        return self.email

class patient(models.Model):
    img=models.ImageField(upload_to='../static/assests')
    gender=models.CharField(max_length=6, choices=(GENDER_CHOICES),default='SELECT')
    type=models.ForeignKey(t,on_delete=models.CASCADE)
    stage=models.CharField(max_length=15,choices=(STAGE_CHOICES),default='STAGE')
    kind=models.ForeignKey(k,on_delete=models.CASCADE)
    cid = models.IntegerField()
    id = models.IntegerField(primary_key=True,unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email=models.EmailField(max_length=40,unique=True)
    phone=models.IntegerField()
    address_a = models.TextField(max_length=60)
    address_b = models.TextField(max_length=60)
    def __str__(self):
        return self.id
 
    

