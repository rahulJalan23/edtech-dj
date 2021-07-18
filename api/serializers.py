from django.core.exceptions import FieldError
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

from drf_queryfields import QueryFieldsMixin



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class CollegeSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    courses = CourseSerializer(Course, many=True, read_only=True)
    branches = BranchSerializer(Branch, many=True, read_only=True)
    class Meta:
        model = College
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    # portions = PortionSerializer(Portion, many=True, read_only=True)
    # portions = serializers.HyperlinkedRelatedField(many=True, view_name="portion-detail", read_only=True)
    class Meta:
        model = Subject
        fields = '__all__'


# class PortionSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Portion
#         fields = '__all__'











# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'first_name', 'last_name',]


# class TextbookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Textbook 
#         fields = '__all__'


# class TimetableSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Timetable
#         fields = '__all__'
    

# class LectureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lecture
#         fields = ['subject', 'start_time', 'end_time', 'teacher']


# class DaySerializer(serializers.ModelSerializer):
#     lectures = LectureSerializer(many=True, read_only=True)
#     class Meta:
#         model = Day
#         fields = "__all__"


# class TimetableSerializer(serializers.ModelSerializer):
#     days = DaySerializer(many=True, read_only=True)
#     class Meta:
#         model = Timetable
#         fields = '__all__'



# class MaterialSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Material 
#         fields = '__all__'



# class FacultySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Faculty
#         fields = '__all__'


# class GsheettableSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Gsheettable
#         fields = '__all__'

