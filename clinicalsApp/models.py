from django.db import models

# Create your models here.
class paitent(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()

class clinicaldata(models.Model):
    component_name=[('hw','HEIGHT/WEIGHT'),('bp','BLOOD PRESSURE'),('heatrtrate','HEART RATE')]
    componentname = models.CharField(max_length=20,choices=component_name)
    componentvalue = models.CharField(max_length=20)
    measuredatetime = models.DateTimeField(auto_now_add=True)
    paitent =models.ForeignKey(paitent,on_delete=models.CASCADE)