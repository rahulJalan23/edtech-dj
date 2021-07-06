from django.contrib import admin
from .models import *

admin.site.register(Textbook)
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Branch)

# Register your models here.
