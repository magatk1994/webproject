from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib import messages
from django.db.models import Q

def index(request):
    query = request.GET.get('searchquery')
    if query:
        students = Student.objects.filter(
            Q(name__icontains=query) |
            Q(reg_no__icontains=query) |
            Q(phone_no__icontains=query) |
            Q(emis_no__icontains=query) |
            Q(aadhaar_no__icontains=query)
        )
    else:
        students = Student.objects.all()

    return render(request, 'index.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        reg_no = request.POST.get('reg_no')
        name = request.POST.get('name')
        aadhaar_no = request.POST.get('aadhaar_no')
        emis_no = request.POST.get('emis_no')
        phone_no = request.POST.get('phone_no')

        Student.objects.create(
            reg_no=reg_no,
            name=name,
            aadhaar_no=aadhaar_no,
            emis_no=emis_no,
            phone_no=phone_no
        )
        messages.success(request, 'Student added successfully!')
        return redirect('index')


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.reg_no = request.POST.get('reg_no')
        student.name = request.POST.get('name')
        student.aadhaar_no = request.POST.get('aadhaar_no')
        student.emis_no = request.POST.get('emis_no')
        student.phone_no = request.POST.get('phone_no')
        student.save()
        messages.success(request, 'Student updated successfully!')
        return redirect('index')


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('index')
