from django.db import models



class employee_registration(models.Model):
    FIRSTNAME= models.CharField(max_length=100,null=True)
    LASTNAME= models.CharField(max_length=100,null=True)
    dob= models.CharField(max_length=100,null=True)
    phonenumber= models.CharField(max_length=100,null=True)
    emailid= models.CharField(max_length=100,null=True)
    GENDER=  models.CharField(max_length=100,null=True)

class other_detail(models.Model):
    FATHERNAME= models.CharField(max_length=100,null=True)
    MOTHERNAME= models.CharField(max_length=100,null=True)
    Address= models.CharField(max_length=100,null=True)
    City= models.CharField(max_length=100,null=True)
    Zip= models.CharField(max_length=100,null=True)
    Aadharnumber= models.CharField(max_length=100,null=True)
    Driverlicense= models.CharField(max_length=100,null=True)
    emergencycontactno2= models.CharField(max_length=100,null=True)
    emergencycontactno1= models.CharField(max_length=100,null=True)

class ed_det(models.Model):
    qualification= models.CharField(max_length=100,null=True)
    institute= models.CharField(max_length=100,null=True)
    year= models.CharField(max_length=100,null=True)
    percent= models.CharField(max_length=100,null=True)

class ex_det(models.Model):
    company= models.CharField(max_length=100,null=True)
    from_date= models.CharField(max_length=100,null=True)
    to_date= models.CharField(max_length=100,null=True)
    position= models.CharField(max_length=100,null=True)
    reason= models.CharField(max_length=100,null=True)
    

class employee_salary_details(models.Model):
    designation= models.CharField(max_length=100,null=True)
    salary= models.CharField(max_length=100,null=True)
    DATE= models.CharField(max_length=100,null=True)
    MONTH= models.CharField(max_length=100,null=True)
    YEAR= models.CharField(max_length=100,null=True)
    

class bank_det(models.Model):
    accountnumber= models.CharField(max_length=100,null=True)
    ifsccode= models.CharField(max_length=100,null=True)
    bankname= models.CharField(max_length=100,null=True)
    bankaddress= models.CharField(max_length=100,null=True)
    
class user_man(models.Model):
    username= models.CharField(max_length=100,null=True)
    password= models.CharField(max_length=100,null=True)
    role=models.CharField(max_length=100,null=True)
    