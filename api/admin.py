from django.contrib import admin
from .models import *

class LectureInline(admin.TabularInline):
    model = Timetable.lectures.through

class TimetableAdmin(admin.ModelAdmin):
    inlines = [
        LectureInline,
    ]


class TextbookInline(admin.StackedInline):
    model = Textbook
    fields = ['title']

class SubjectAdmin(admin.ModelAdmin):
    inlines = [
        TextbookInline
    ]

class CourseAdmin(admin.ModelAdmin):
    inlines = [
        TextbookInline
    ]  

class BranchAdmin(admin.ModelAdmin):
    inlines = [
        TextbookInline
    ] 

admin.site.register(Textbook)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Lecture)
admin.site.register(Timetable, TimetableAdmin)

# Register your models here.
