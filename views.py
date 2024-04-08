from django.shortcuts import render, HttpResponse
from .models import Student
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'function_view/index.html')

def list(request):
    students = Student.objects.all()
    context = {
        'students':students
    }
    return render(request, 'function_view/list.html', context)

def detail(request, id):
    student = Student.objects.get(pk=id)
    context = {
        'student':student
    }
    return render(request, 'function_view/detail.html', context)

def add(request):
    if request.method == "POST":
        data = Student()
        data.first_name = request.POST['first_name']
        data.last_name = request.POST['last_name']
        data.save()
        return HttpResponseRedirect('/function_view/list/')
    return render(request, 'function_view/add.html')

def update(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student':student
    }
    return render(request, 'function_view/update.html', context)

def update_record(request, id):
    if request.method == "POST":
        data = Student.objects.get(id=id)
        data.first_name = request.POST['first_name']
        data.last_name = request.POST['last_name']
        data.save()
        return HttpResponseRedirect('/function_view/list/')

def delete(request, id):
    if request.method == "POST":
        student = Student.objects.get(id=id)
        student.delete()
        return HttpResponseRedirect('/function_view/list/')
    else:
        student = Student.objects.get(id=id)
        context = {
            'student':student
        }
        return render(request, 'function_view/delete.html', context)