from operator import mod
from django.db import models

# Create your models here.


class Superuser(models.Model):
    rogno=models.PositiveBigIntegerField()
    name=models.CharField(max_length=255)
    mail=models.EmailField()
    phone=models.PositiveBigIntegerField()


class Usrdata(models.Model):
    rogno=models.PositiveBigIntegerField()
    name=models.CharField(max_length=255)
    mail=models.EmailField()
    phone=models.PositiveBigIntegerField()
    adv_id=models.ForeignKey(Superuser,on_delete=models.PROTECT)

class Leavedata(models.Model):
    rogno=models.PositiveBigIntegerField()
    startdate=models.DateField(null=True)
    enddate=models.DateField(null=True)
    ref_id=models.ForeignKey(Usrdata,on_delete=models.PROTECT)
    name=models.CharField(max_length=255)
    reasontype=models.CharField(max_length=255,null=True)
    reason=models.TextField()
    status=models.CharField(max_length=255)