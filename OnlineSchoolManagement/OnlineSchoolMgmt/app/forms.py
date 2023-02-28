from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 
 
class addAttendanceform(ModelForm):
    class Meta:
        model=Attendance
        fields="__all__"
 
class addMarksform(ModelForm):
    class Meta:
        model=Marks
        fields="__all__"
 
class addNoticeform(ModelForm):
    class Meta:
        model=Notice
        fields="__all__"