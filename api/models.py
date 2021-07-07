from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.utils import timezone

# Create your models here.

"""
MODELS:
    - SUBJECT:
        fields : name, description, code.

    - BRANCHES: 
        fields : name, description

    - COURSE:
        fields : name, description

    - TEXTBOOK:
        fields : title, description, author, link, cover_image, subject, date_posted, posted_by.

"""

class Subject(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    subject_code = models.CharField(max_length=6)

    def __str__(self):
        return self.subject_code


class Branch(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    branch_code = models.CharField(max_length=6, default="")

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    course_code = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.name


class Textbook(models.Model):
    YEARS = [
        ('FIRST', 'FIRST'),
        ('SECOND', 'SECOND'),
        ('THIRD', 'THIRD'),
        ('FOURTH', 'FOURTH'),
    ]

    title = models.CharField(max_length=150)
    author = models.CharField(max_length=60)
    link = models.URLField(max_length=200)
    cover_image = models.URLField(max_length=200)
    subject = models.CharField(max_length=40)
    subject_code = models.CharField(max_length=6, default="")
    branch_code = models.CharField(max_length=6, default="")
    course_code = models.CharField(max_length=10, default="")
    year = models.CharField(max_length=8,choices=YEARS, default='FIRST')
    posted_by = models.CharField(max_length=20)
    date_posted = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return self.title



class Timetable(models.Model):
    YEARS = [
        ('FIRST', 'FIRST'),
        ('SECOND', 'SECOND'),
        ('THIRD', 'THIRD'),
        ('FOURTH', 'FOURTH'),
    ]

    title = models.CharField(max_length=150)
    branch_code = models.CharField(max_length=6, default="")
    course_code = models.CharField(max_length=10, default="")
    year = models.CharField(max_length=8,choices=YEARS, default='FIRST')

    def __str__(self):
        return self.title


class Lecture(models.Model):
    DAYS = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]

    day = models.CharField(max_length=10, choices=DAYS, default='')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    teacher = models.CharField(max_length=60)
    timetables = models.ManyToManyField(Timetable, related_name='lectures')


    def __str__(self):
        return f"Lecture on {self.subject.subject_code} by {self.teacher} ( {self.day}, {self.start_time} - {self.end_time})"


"""
Timetable
{
    Mon : [
        {
            'subject_code': ,
            'from': ,
            'to': ,
            'teacher':
        },
        {},
        {},
        {},      
    ],
    Tue: ,
    wed: ,
}
"""
