from django.db import models

class tbl_district(models.Model):
    district_name=models.CharField(max_length=30)


class tbl_brand(models.Model):
    brand_name=models.CharField(max_length=30) 

class tbl_category(models.Model):
    category_name=models.CharField(max_length=30)


class tbl_register(models.Model):
    admin_name=models.CharField(max_length=30) 
    admin_email=models.CharField(max_length=30)
    admin_pass=models.CharField(max_length=30)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_chatbot(models.Model):
    questions=models.CharField(max_length=50)
    answers=models.CharField(max_length=50)

class tbl_type(models.Model):
    type=models.CharField(max_length=50) 

      
class tbl_crop(models.Model):
    crop_name=models.CharField(max_length=50)

class tbl_fertilizer(models.Model):
    fert_name=models.CharField(max_length=50)
    fert_details=models.CharField(max_length=50)
    crop=models.ForeignKey(tbl_crop,on_delete=models.CASCADE)

class tbl_pest(models.Model):
    pest=models.CharField(max_length=50)
    crop=models.ForeignKey(tbl_crop,on_delete=models.CASCADE)    
      
