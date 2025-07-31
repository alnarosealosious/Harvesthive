from django.db import models
from Guest.models import *
from Owner.models import *

class tbl_Predict(models.Model):
     temperature=models.CharField(max_length=30)
     soiltype=models.CharField(max_length=30)
     soildepth=models.CharField(max_length=30)
     rainfall=models.CharField(max_length=30)
     predict_result=models.CharField(max_length=30)
     user=models.ForeignKey(tbl_user,on_delete=models.CASCADE) 

class tbl_pestdetect(models.Model):
     pest_name=models.CharField(max_length=30)
     pest_result=models.CharField(max_length=30)
     pest_date=models.DateField(max_length=30)
     user=models.ForeignKey(tbl_user,on_delete=models.CASCADE) 

class tbl_fertilizerdetect(models.Model):
    fertil_name=models.CharField(max_length=30)
    fert_result=models.CharField(max_length=30)
    fert_date=models.DateField(max_length=30)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)        
                 
class tbl_addrequest(models.Model):
     req_content=models.CharField(max_length=30)
     user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
     plot=models.ForeignKey(tbl_plot,on_delete=models.CASCADE)
     req_status=models.IntegerField(default=0)        

# Create your models here.
