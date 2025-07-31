from django.db import models
from Admin.models import *
from Guest.models import *

    
class tbl_complain(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True) 
    comp_reply=models.CharField(max_length=50)
    comp_status=models.IntegerField(default=0)
    owner=models.ForeignKey(tbl_owner,on_delete=models.CASCADE,null=True) 
          
class tbl_plot(models.Model):
    landmetrics=models.CharField(max_length=30)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    owner=models.ForeignKey(tbl_owner,on_delete=models.CASCADE)
    plot_status=models.IntegerField(default=0)

class tbl_condition(models.Model):
    content=models.CharField(max_length=50)
    plot=models.ForeignKey(tbl_plot,on_delete=models.CASCADE)      

class tbl_gallery(models.Model):
    photo=models.FileField(upload_to="Assests/Owner/")
    plot_id=models.ForeignKey(tbl_plot,on_delete=models.CASCADE)    

class tbl_plottype(models.Model):
    plot=models.ForeignKey(tbl_plot,on_delete=models.CASCADE)
    Type=models.ForeignKey(tbl_type,on_delete=models.CASCADE)

# Create your models here.
