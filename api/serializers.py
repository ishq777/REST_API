from rest_framework import serializers
from students.models import Student
from employees.models import Employee
from blogs.serializers import CommentSerializer

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = "__all__"
        