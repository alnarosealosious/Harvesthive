from django.db import models
from Admin.models import *


class tbl_user(models.Model):
    user_name=models.CharField(max_length=30)
    user_address=models.CharField(max_length=30)
    user_contact=models.CharField(max_length=30)
    user_email=models.CharField(max_length=30)
    user_photo=models.FileField(upload_to="Assests/User/")
    user_pass=models.CharField(max_length=30)
    user_confirm=models.CharField(max_length=30)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)

class tbl_owner(models.Model):
    owner_name=models.CharField(max_length=30)
    owner_email=models.CharField(max_length=30)
    owner_pass=models.CharField(max_length=30)
    owner_address=models.CharField(max_length=30)
    owner_proof=models.FileField(upload_to="Assests/Owner/")   
    



