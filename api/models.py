import datetime
from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

"""
MODELS:
    - SUBJECT:
        fields : name, description, subject_code.

    - BRANCHES: 
        fields : name, description, branch_code.

    - COURSE:
        fields : name, description, course_code

    - TEXTBOOK:
        fields : title, author, link, cover_image, subject, date_posted, posted_by, description.

"""

class Subject(models.Model):

    """Model for all the Subjects"""

    YEARS = [
        ('FIRST', 'FIRST'),
        ('SECOND', 'SECOND'),
        ('THIRD', 'THIRD'),
        ('FOURTH', 'FOURTH'),
    ]

    name = models.CharField(max_length=150)
    description = models.TextField()
    subject_code = models.CharField(max_length=8, unique=True, primary_key=True)
    year = models.CharField(max_length=8, choices=YEARS, default='FIRST')

    def __str__(self):
        return f"{self.subject_code}: {self.name}"


class Branch(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    branch_code = models.CharField(max_length=8, unique=True, primary_key=True)

    def __str__(self):
        return f"{self.branch_code}: {self.name}"


class Course(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    course_code = models.CharField(max_length=10, unique=True, primary_key=True)

    def __str__(self):
        return f"{self.course_code}: {self.name}"


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
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, related_name="textbooks")
    # subject_code = models.CharField(max_length=6, default="")
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING, related_name="textbooks", blank=True, null=True)
    # branch_code = models.CharField(max_length=6, default="")
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, related_name="textbooks", blank=True, null=True)
    # course_code = models.CharField(max_length=10, default="")
    year = models.CharField(max_length=8,choices=YEARS, default='FIRST')
    posted_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='textbooks')
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

    SEMESTERS = [
        ('SEM_1', "I Semester"),
        ('SEM_2', "II Semester"),
        ('SEM_3', "III Semester"),
        ('SEM_4', "IV Semester"),
        ('SEM_5', "V Semester"),
        ('SEM_6', "VI Semester"),
        ('SEM_7', "VII Semester"),
        ('SEM_8', "VIII Semester"),
        ]

    title = models.CharField(max_length=150)
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING, related_name="timetables")
    # branch_code = models.CharField(max_length=6, default="")
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, related_name="timetables")
    # course_code = models.CharField(max_length=10, default="")
    year = models.CharField(max_length=8,choices=YEARS, default='FIRST')
    semester = models.CharField(max_length=5,choices=SEMESTERS, default='FIRST')

    def __str__(self):
        return self.title


class Day(models.Model):
    DAYS = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]
    day = models.CharField(max_length=3, choices=DAYS, default='MON')
    timetable = models.ForeignKey(Timetable, on_delete=CASCADE, related_name='days', blank=False)

    def __str__(self):
        return f"{self.day} in {self.timetable.title}."


class Lecture(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    teacher = models.CharField(max_length=60)
    days = models.ManyToManyField(Day, related_name='lectures', blank=True)


    def __str__(self):
        return f"Lecture on {self.subject.subject_code} by {self.teacher} ( {self.start_time} - {self.end_time} )"


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


