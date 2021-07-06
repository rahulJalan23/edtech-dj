from django.db import models
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
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.code


class Branch(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name


class Textbook(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=60)
    link = models.URLField(max_length=200)
    cover_image = models.URLField(max_length=200)
    subject = models.CharField(max_length=40)
    # subject_code = models.CharField(max_length=6)
    posted_by = models.CharField(max_length=20)
    date_posted = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return self.title

class Timetable(models.Model):
    pass

class Day(models.Model):
    pass

class Period(models.Model):
    pass


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
