from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (Day, Portion, 
                     Subject,
                     Branch,
                     Course,
                     Textbook,
                     Timetable,
                     Lecture)

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name',]


class TextbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Textbook 
        fields = '__all__'


class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'
    

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['subject', 'start_time', 'end_time', 'teacher']


class DaySerializer(serializers.ModelSerializer):
    lectures = LectureSerializer(many=True, read_only=True)
    class Meta:
        model = Day
        fields = "__all__"


class TimetableSerializer(serializers.ModelSerializer):
    days = DaySerializer(many=True, read_only=True)
    class Meta:
        model = Timetable
        fields = '__all__'


class PortionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portion
        fields = '__all__'

    

