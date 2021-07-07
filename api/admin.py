from django.contrib import admin
from .models import *

class LectureInline(admin.TabularInline):
    model = Timetable.lectures.through

class TimetableAdmin(admin.ModelAdmin):
    inlines = [
        LectureInline,
    ]


admin.site.register(Textbook)
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Branch)
admin.site.register(Lecture)
admin.site.register(Timetable, TimetableAdmin)

# Register your models here.
