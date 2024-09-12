from django.shortcuts import render, redirect
from clinicalsApp.models import paitent, clinicaldata
from django.views.generic import ListView ,CreateView,DeleteView,UpdateView,DetailView
from django.urls import reverse_lazy
from clinicalsApp.forms import clinicaldataform
# Create your views here.
class paitentlistview(ListView):
    model=paitent

class paitentdetailview(DetailView):
    model=paitent
    fields=('firstname','lastname','age')

class paitentcreateview(CreateView):
    model=paitent
    success_url = reverse_lazy('index')
    fields=('firstname','lastname','age')
    

class paitentupdateview(UpdateView):
    model=paitent
    fields=('firstname','lastname','age')
    success_url=reverse_lazy('index')

class paitentdeleteview(DeleteView):
    model=paitent
    success_url=reverse_lazy('index')


def adddata(request,**kwargs):
    form=clinicaldataform()
    paitents=paitent.objects.get(id=kwargs['pk'])
    if request.method=='POST':
        form=clinicaldataform(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')    
    return render(request,'clinicalsApp/clinicaldata_form.html',{'form':form , 'paitent':paitents})

def analyse(request,**kwargs):
    data = clinicaldata.objects.filter(paitent_id=kwargs['pk'])
    responseData= []
    for eachentry in data:
        if eachentry.componentname =='hw':
            heightandweight = eachentry.componentvalue.split('/')
            if len(heightandweight) >1:
                feettometer = float(heightandweight[0])*0.4536
                BMI = (float(heightandweight[1]))/(feettometer*feettometer)
                BMIentry=clinicaldata()
                BMIentry.componentname = 'BMI'
                BMIentry.componentvalue = BMI
                BMIentry.measuredatetime = '---'
                responseData.append(BMIentry)
        responseData.append(eachentry)    

    return render(request,'clinicalsApp/GenerateReport.html',{'data':responseData})