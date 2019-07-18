from django import forms
from crudapplication.models import Employee,UserProfileInfo,User

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')