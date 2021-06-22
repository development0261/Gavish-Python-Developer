from rest_framework import serializers
from .models import Employee,Department,Designation,EmployeeSlots
class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(

        read_only=True,
        slug_field='name'
    )

    designation = serializers.SlugRelatedField(

        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Employee
        fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class EmployeeSlitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSlots
        fields = "__all__"