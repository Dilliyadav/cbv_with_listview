from django.db import models

# Create your models here.
class school(models.Model):
    sname=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    sloc=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.sname


class student(models.Model):
    sname=models.ForeignKey(school,on_delete=models.CASCADE)
    stname=models.CharField(max_length=100)
    sage=models.IntegerField()

