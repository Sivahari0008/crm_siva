from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from .models import*
from .forms import*

def add(request,id=0):
    if(request.method =="GET"):
        if(id==0):
            form = employee_registration_forms()
            form_2= other_detail_forms()
            form_3= ed_det_forms()
            form_4= ex_det_forms()
        else:            
            id_value=employee_registration.objects.get(id=id)
            form =employee_registration_forms(instance = id_value)
            id_value_2=other_detail.objects.get(id=id)
            form_2=other_detail_forms(instance = id_value_2)
            id_value_3= ed_det.objects.get(id=id)
            form_3 = ed_det_forms(instance = id_value_3)
            id_value_4= ex_det.objects.get(id=id)
            form_4 = ex_det_forms(instance = id_value_4)
        return render(request,'forms4.html')
    else:
        if(id ==0):        
            form=employee_registration_forms(request.POST)
            form_2=other_detail_forms(request.POST) 
            form_3=ed_det_forms(request.POST)
            form_4=ex_det_forms(request.POST)      
        else:
            id_value = employee_registration.objects.get(id=id)
            form = employee_registration_forms(request.POST,instance = id_value)
            id_value_2= other_detail.objects.get(id=id)
            form_2 = other_detail_forms(request.POST,instance = id_value_2)
            id_value_3 = ed_det.objects.get(id=id)
            form_3 = ed_det_forms(request.POST,instance = id_value_3)
            id_value_4 = ex_det.objects.get(id=id)
            form_4 = ex_det_forms(request.POST,instance = id_value_4)
        if (form.is_valid()):
                form.save()
        if (form_2.is_valid()):                
                form_2.save()        
        all_form_2=other_detail.objects.all()
        all_data=employee_registration.objects.all()
        if (form_4.is_valid()):                  
                form_4.save()
        if (form_3.is_valid()):        
                form_3.save()     
        for i in range(1,(int(request.POST["totallen"]))+1):
            ae=ex_det(company=request.POST["company"+str(i)],from_date=request.POST["from_date"+str(i)],to_date=request.POST["to_date"+str(i)],position=request.POST["position"+str(i)],reason=request.POST["reason"+str(i)])
            ae.save()              
        for i in range(1,(int(request.POST["totallength"]))+1):
            aa=ed_det(qualification=request.POST["qualification"+str(i)],institute=request.POST["institute"+str(i)],year=request.POST["year"+str(i)],percent=request.POST["percent"+str(i)])
            aa.save()
        all_data_3=ed_det.objects.all()  
        all_data_4=ex_det.objects.all()
        return redirect('forms5.html')
        

def sub(request,id=0):
    if(request.method =="GET"):
        if(id==0):
            form_5 = employee_salary_details_forms()
            form_6 = bank_detforms()
        else:            
            id_value_5=employee_salary_details.objects.get(id=id)
            form_5 =employee_salary_details_forms(instance = id_value_5)
            id_value_6=bank_det.objects.get(id=id)
            form_6 =bank_detforms(instance = id_value_6)
        return render(request,'forms5.html')
    else:
        if(id ==0):        
            form_5=employee_salary_details_forms(request.POST)
            form_6=bank_detforms(request.POST)     
        else:
            id_value_5 = employee_salary_details.objects.get(id=id)
            form_5 = employee_salary_details_forms(request.POST,instance = id_value_5)
            id_value_6 = employee_salary_details.objects.get(id=id)
            form_6 = bank_detforms(request.POST,instance = id_value_6)
        if (form_5.is_valid()):
                form_5.save()
        if (form_6.is_valid()):
                form_6.save()
        all_data_5=employee_salary_details.objects.all()
        all_data_6=bank_det.objects.all()
        return redirect('forms4.html') 

