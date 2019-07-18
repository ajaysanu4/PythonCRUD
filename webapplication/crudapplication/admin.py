from django.contrib import admin
from .models import Employee
from django.contrib import admin
from crudapplication.models import UserProfileInfo, User

admin.site.register(Employee)

# Register your models here.
admin.site.register(UserProfileInfo)