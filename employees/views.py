from django.db.models import Q
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

from .serializers import EmployeeSerializer
# Create your views here.
from .models import *

def index(request):
    return render(request,'index.html')

@api_view(['GET','POST'])
def employees(request):

    employees_data = Employee.objects.all()
    serialized_emp = EmployeeSerializer(employees_data, many=True)
    message={'status':'success'}
    return Response(serialized_emp.data)

@api_view(['GET','POST'])
def getEmplpyee(request):
    employees_data = Employee.objects.all()
    serialized_emp = EmployeeSerializer(employees_data, many=True)
    return Response(serialized_emp.data)

@api_view(['GET','POST'])
def getAvailableSlots(request,id,id2):
    slots_list = [
        '09:00 AM to 10:00 AM',
        '10:00 AM to 11:00 AM',
        '11:00 AM to 12:00 AM',
        '12:00 PM to 01:00 PM',
        '01:00 PM to 02:00 PM',
        '02:00 PM to 03:00 PM',
        '03:00 PM to 04:00 PM',
        '04:00 PM to 05:00 PM',
        '05:00 PM to 06:00 PM'

    ]

    booked_meetings = EmployeeSlots.objects.filter(Q(employee1=Employee.objects.get(employeeid=id)) | Q(employee1=Employee.objects.get(employeeid=id2)), is_completed=False)
    booked_meetings1 = EmployeeSlots.objects.filter(Q(employee2=Employee.objects.get(employeeid=id)) | Q(employee2=Employee.objects.get(employeeid=id2)), is_completed=False)




    booked_slots = []
    for meet in booked_meetings:
        booked_slots.append(meet.meetingfromtime+ " to " + meet.meetingtotime )
    for meet in booked_meetings1:
        booked_slots.append(meet.meetingfromtime+ " to " + meet.meetingtotime )

    print(booked_slots)
    slots_to_send = []

    for slots in slots_list:

        if slots.strip() not in booked_slots:
            slots_to_send.append(slots)

    return Response(slots_to_send)


@api_view(['POST'])
def bookAppointment(request):
    if request.method == "POST":
        emp1 = request.POST['emp1']
        emp2 = request.POST['emp2']
        time = request.POST['time']

        from_time = time[0:8]
        to_time = time[-8:]
        emp_meeting = EmployeeSlots(employee1=Employee.objects.get(employeeid=emp1),employee2=Employee.objects.get(employeeid=emp2),meetingfromtime=from_time,meetingtotime=to_time)
        emp_meeting.save()



        return redirect("HomePage")


