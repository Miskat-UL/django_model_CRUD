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


def show(request, *args, **kwargs):
    if request.method == "GET":
        query = Teachers.objects.all()
        context = {
            "object": query
        }
        return render(request, 'teacher_show.html', context)


def search(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, "teacher_search.html")
    elif request.method == "POST":
        name = request.POST['search']

        value = Teachers.objects.get(name=name)

        context = {
            "tea": value
        }
        return render(request, "teacher_search.html", context)





def another(request, edit, qs):
    if edit == "delete":
        student = Teachers.objects.get(id=qs)
        student.delete()
    if edit == "edit":
        if request.method == "GET":
            teachers = Teachers.objects.get(id=qs)
            context = {
                'teacher': teachers
            }

            return render(request, 'teacher_edit.html', context)
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            course = request.POST['course']
            number = request.POST['number']

            teacher = Teachers.objects.get(id=qs)

            teacher.name = name
            teacher.email = email
            teacher.course = course
            teacher.phone = number

            teacher.save()

    return redirect('/teachers')
