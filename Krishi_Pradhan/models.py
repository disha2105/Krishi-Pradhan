from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    email = models.EmailField(max_length=100)
    password1 =models.CharField(max_length=45)
    password2 = models.CharField(max_length=45)

class question(models.Model):
    region= models.CharField(max_length=100)
    soil = models.CharField(max_length=100)
    previous= models.CharField(max_length=100)

class cropdata(models.Model):
    id=models.IntegerField(primary_key=True)
    region1=models.CharField(max_length=255)
    soil1=models.CharField(max_length=255)
    crop1=models.CharField(max_length=255)
    class meta:
        db_table= 'kkrishi_pradhan_cropdata'