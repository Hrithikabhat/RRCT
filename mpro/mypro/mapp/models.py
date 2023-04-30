from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
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
KIND_CHOICES=(
    ("KIND", "KIND"),
    ("HODGKIN LYMPHOMA", "HODGKIN LYMPHOMA"),
    ("NON-HODGKIN LYMPHOMA", "NON-HODGKIN LYMPHOMA"),
    ("MULTIPLE LYMPHOMA", "MULTIPLE LYMPHOMA"),
    ("NON-RECURRENT", "NON-RECURRENT"),
    ("LOCALLY-ADVANCED", "LOCALLY-ADVANCED"),
    ("RECURRENT", "RECURRENT"),
    ("NON-SMALL CELL", "NON-SMALL CELL"),
    ("SMALL CELL", "SMALL CELL"),
    ("BASAL CELL CARCINOMA", "BASAL CELL CARCINOMA"),
    ("SQUAMOUS CELL CARCINOMA", "SQUAMOUS CELL CARCINOMA"),
    ("MERKEL CELL CARCINOMA", "MERKEL CELL CARCINOMA"),
)
# Create your models here.

class patient(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    img=models.ImageField(upload_to='../static/assests')
    gender=models.CharField(max_length=6, choices=(GENDER_CHOICES),default='SELECT')
    type=models.CharField(max_length=15,choices=(TYPE_CHOICES),default='TYPE')
    stage=models.CharField(max_length=15,choices=(STAGE_CHOICES),default='STAGE')
    kind=models.CharField(max_length=35,choices=(KIND_CHOICES),default='KIND')
    clid = models.IntegerField(default=0)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email=models.EmailField(max_length=40,unique=True)
    phone=PhoneNumberField()
    address_a = models.TextField(max_length=60)
    address_b = models.TextField(max_length=60)
    def __str__(self):
        return self.email
 
class clinic(models.Model):
    cid = models.IntegerField(primary_key=True,unique=True)
    cname = models.CharField(max_length=30)
    cemail=models.EmailField(max_length=40)
    def __str__(self):
        return self.cemail






