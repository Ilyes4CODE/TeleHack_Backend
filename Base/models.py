from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Center(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    adress =  models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    Home_number = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class TicketCenter(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=2500)
    Center = models.ForeignKey(Center,on_delete=models.CASCADE)
    place = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Title

class TicketTech(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=2500)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    phone_number = models.CharField(max_length=50,null=True)
    center = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=50,null=True)
    place = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Title




class FeedBack(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    center = models.CharField(max_length=50,null=True)    
    def __str__(self):
        return self.Title
    

    
    