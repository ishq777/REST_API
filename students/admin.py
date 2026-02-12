from django.contrib import admin
from .models import Student


class StudentAdminView(admin.ModelAdmin):
    list_display = ['student_id', 'name', 'branch']

admin.site.register(Student, StudentAdminView)

# Register your models here.
