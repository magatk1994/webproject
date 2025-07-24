from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'reg_no', 'name', 'aadhaar_no', 'emis_no', 'phone_no')
    search_fields = ('reg_no', 'name', 'aadhaar_no', 'emis_no', 'phone_no')

