from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.CharField(max_length=100)
    econtact = models.CharField(max_length=15)
    class meta:
        db_table ="employee"


# Create your models here.
class UserProfileInfo(models.Model):
   user = models.OneToOneField(User,on_delete=models.CASCADE)
   portfolio_site = models.URLField(blank=True)
   profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

   def __str__(self):
    return self.user.username