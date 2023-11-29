from django.db import models

class User(models.Model):
    username=models.CharField(primary_key=True,max_length=20)
    password=models.CharField(null=False,max_length=20)
    name=models.CharField(null=False,max_length=30)
    phone_no=models.CharField(null=False,max_length=13)
    email=models.CharField(null=False,max_length=255)
    test_attempted=models.IntegerField()
    points=models.FloatField()

class Questions(models.Model):
    qid=models.BigAutoField(primary_key=True,auto_created=True)
    que=models.TextField()
    a=models.CharField(max_length=255)
    b=models.CharField(max_length=255)
    c=models.CharField(max_length=255)
    d=models.CharField(max_length=255)
    ans=models.CharField(max_length=2)

class Result(models.Model):
    resultid=models.BigAutoField(primary_key=True,auto_created=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)
    attempt=models.IntegerField()
    right=models.IntegerField()
    wrong=models.IntegerField()
    points=models.FloatField()