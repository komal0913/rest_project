from django.shortcuts import render
from . models import employees
from . serializers import employeesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class employeeList(APIView):

	def get(self, request):
		emp_1 = employees.objects.all()
		serializer = employeesSerializer(emp_1, many=True)
		return Response(serializer.data)
