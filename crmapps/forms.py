from django.forms import ModelForm
from django import forms
from .models import *



class employee_registration_forms(forms.ModelForm):
    class Meta:
        model= employee_registration
        fields={'FIRSTNAME','LASTNAME','phonenumber','emailid','dob','GENDER'}
        widgets={
            
            'FIRSTNAME':forms.TextInput(attrs={'class':'form-control','placeholder':'firstname'}),
            'LASTNAME': forms.TextInput(attrs={'class':'form-control','placeholder':'lastname'}),
            'dob':forms.TextInput(attrs={'class':'form-control'}),
            'phonenumber': forms.TextInput(attrs={'class':'form-control','placeholder':'Companyname'}),
            'emailid': forms.TextInput(attrs={'class':'form-control','placeholder':'lastname'}),
            'GENDER': forms.TextInput(attrs={'class':'form-control','placeholder':'lastname'}),
         
        }

        
class other_detail_forms(forms.ModelForm):
    class Meta:
        model= other_detail
        fields={'FATHERNAME','MOTHERNAME','City','Zip','Address','emergencycontactno2','Driverlicense','Aadharnumber','emergencycontactno1'}
        widgets={
            
            'FATHERNAME': forms.TextInput(attrs={'class':'form-control','placeholder':'Companyname'}),
            'MOTHERNAME': forms.TextInput(attrs={'class':'form-control','placeholder':'lastname'}),
            'City': forms.TextInput(attrs={'class':'form-control','placeholder':'Companyname'}),
            'Zip':forms.TextInput(attrs={'class':'form-control','placeholder':'Companyname'}),
            'Address':forms.TextInput(attrs={'class':'form-control','placeholder':'Companyname'}),
            'Driverlicense': forms.TextInput(attrs={'class':'form-control','placeholder':'Companyname'}),
            'Aadharnumber': forms.TextInput(attrs={'class':'form-control','placeholder':'lastname'}),
            'emergencycontactno2': forms.TextInput(attrs={'class':'form-control','placeholder':'Companyname'}),
            'emergencycontactno1': forms.TextInput(attrs={'class':'form-control','placeholder':'lastname'}),
            
        }

class ed_det_forms(forms.ModelForm):
    class Meta:
        model= ed_det
        fields= {'qualification','institute','year','percent'}
        widgets={
            
            'qualification': forms.TextInput(attrs={'class':'form-control','placeholder':'lastname'}),
            'year':forms.TextInput(attrs={'class':'form-control'}),
            'institute': forms.TextInput(attrs={'class':'form-control','placeholder':'Companyname'}),
            'percent': forms.TextInput(attrs={'class':'form-control','placeholder':'lastname'}),
            
            
        }

class ex_det_forms(forms.ModelForm):
    class Meta:
        model= ex_det
        fields= {'from_date','to_date','position','reason','company'}
        widgets={
            'company':forms.TextInput(attrs={'class':'form-control'}),
            'from_date':forms.DateInput(format=('%d-%m-%Y'),attrs={'type':'date','class': 'form-control'}),
            'to_date':forms.DateInput(format=('%d-%m-%Y'),attrs={'type':'date','class': 'form-control'}),
            'position':forms.TextInput(attrs={'class':'form-control'}),
            'reason':forms.TextInput(attrs={'class':'form-control'}),
            }

class employee_salary_details_forms(forms.ModelForm):
    class Meta:
        model= employee_salary_details
        fields={'designation','salary','DATE','MONTH','YEAR'}
        widgets={
            
            'designation': forms.TextInput(attrs={'class':'form-control'}),
            'salary': forms.TextInput(attrs={'class':'form-control'}),
            'DATE':forms.TextInput(attrs={'class':'form-control'}),
            'MONTH':forms.TextInput(attrs={'class':'form-control'}),
            'YEAR':forms.TextInput(attrs={'class':'form-control'}),
            
            
        }

class bank_detforms(forms.ModelForm):
    class Meta:
        model= bank_det
        fields={'accountnumber','ifsccode','bankname','bankaddress'}
        widgets={
            
            'accountnumber': forms.TextInput(attrs={'class':'form-control'}),
            'ifsccode': forms.TextInput(attrs={'class':'form-control'}),
            'bankname': forms.TextInput(attrs={'class':'form-control'}),
            'bankaddress': forms.TextInput(attrs={'class':'form-control'}),
            
            
        }

class user_manforms(forms.ModelForm):
    class Meta:
        model= user_man
        fields={'username','password','role'}
        widgets={
            
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
            'role': forms.TextInput(attrs={'class':'form-control'}),
            
        }
 