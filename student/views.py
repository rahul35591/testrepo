from student.serializers import Studentserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from student.models import Student
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
import json
from django.http import JsonResponse,HttpResponse


def getAllstudents(request):

    students = Student.objects.all()
    serializer = Studentserializer(students,many=True)
    return HttpResponse(students,content_type="application/json")

@api_view(['POST'])
def createStudent(request):
        print('inside create emp')
        print(request.data)
        student = request.data
        s = Student(sname=student['sname'],saddress=student['saddress'],smarks=student['smarks'])
        s.save()
        print('Emp saved successfully...!')
        return Response({"message": "Success"})

