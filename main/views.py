from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student


def home(request):
    if request.method == "GET":
        students = Student.objects.all()
        context = {
            'student': students
        }

        return render(request, 'main.html', context)

    elif request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        blood = request.POST['b_group']
        number = request.POST['number']
        varsity_id = "181-15-10431"

        Student.objects.create(name=name, blood_group=blood, phone=number, email=email, varsity_id=varsity_id)
        return redirect("/students")


def search(request, pk):
    if request.method == "GET":
        return render(request, 'main.html')
    elif request.method == "POST":
        obj = Student.objects.get(pk=id)
        context = {
            'std': obj
        }
        return render(request, 'main.html', context)


def action_handler(request, action, id):
    return HttpResponse("hello")


def another(request, edit, qs):
    if edit == "delete":
        student = Student.objects.get(id=qs)
        student.delete()
    if edit == "edit":
        if request.method == "GET":
            student = Student.objects.get(id=qs)
            context = {
                'student': student
            }

            return render(request, 'edit_eile.html', context)
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            blood = request.POST['b_group']
            number = request.POST['number']

            student = Student.objects.get(id=qs)

            student.name = name
            student.email = email
            student.blood_group = blood
            student.phone = number

            student.save()

    return redirect('/students')







