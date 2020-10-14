from rest_framework import serializers
from . models import employees

class employeesSerializer(serializers.Serializer):

	class Meta:
		models = employees
		fields = '__all__'