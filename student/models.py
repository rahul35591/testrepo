from django.db import models

# Create your models here.

class Student(models.Model):
    sid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    saddress = models.CharField(max_length=50)
    smarks = models.IntegerField()

    class Meta:
        db_table = 'stud'

    def __str__(self):
        return '\n Student ID: {} Student Name:{}  Student Address :{} Student Marks{}'.format(self.sid,self.sname,self.saddress,self.smarks)

    def __repr__(self):
        return str(self)
