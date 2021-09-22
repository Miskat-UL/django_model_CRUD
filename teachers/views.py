from django.shortcuts import render, redirect
from .models import Teachers


def home(request):
    if request.method == "GET":
        teachers = Teachers.objects.all()
        context = {
            'teacher': teachers
        }

        return render(request, 'teachers.html', context)

    if request.method == "POST":
        t_name = request.POST['name']
        t_email = request.POST['email']
        course = request.POST['b_group']
        number = request.POST['number']

        Teachers.objects.create(name=t_name, course=course, phone=number, email=t_email)

        return redirect("/teachers")




