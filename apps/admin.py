import csv

from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.db.models import Count
from django.http import HttpResponse

from apps.models import University, Student


class StudentAdmin(admin.StackedInline):
    list_display = ('first_name', 'last_name', 'university')
    model = Student
    extra = 1
