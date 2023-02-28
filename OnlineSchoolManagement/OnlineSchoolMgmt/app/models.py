from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Attendance(models.Model):
    StudentName = models.CharField(max_length=200,null=True)
    StudentId  = models.CharField(max_length=50,null=True)
    LecturesAttended = models.IntegerField(null=True)
    TotalLectures  = models.IntegerField(null=True)
 
    def __str__(self):
        return self.StudentName
 
class Marks(models.Model):
    StudentName = models.CharField(max_length=200,null=True)
    StudentId  = models.CharField(max_length=50,null=True)
    PhysicsMarks = models.IntegerField(null=True)
    ChemistryMarks  = models.IntegerField(null=True)
    MathsMarks  = models.IntegerField(null=True)
    EnglishMarks  = models.IntegerField(null=True)
    ComputerMarks  = models.IntegerField(null=True)
 
    def __str__(self):
        return self.StudentName
 
class Notice(models.Model):
    Message = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Message
