from django.shortcuts import render, redirect
from .models import Course


def home(request):
    return render(request, 'courses/home.html')


def add_course(request):
    if request.method == 'POST':
        course_name = request.POST['course_name']
        course_code = request.POST['course_code']
        duration = request.POST['duration']
        fee = request.POST['fee']

        Course.objects.create(
            course_name=course_name,
            course_code=course_code,
            duration=duration,
            fee=fee
        )

        return redirect('view_courses')

    return render(request, 'courses/add_course.html')


def view_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/view_courses.html', {'courses': courses})
def edit_course(request, id):
    course = Course.objects.get(id=id)

    if request.method == 'POST':
        course.course_name = request.POST['course_name']
        course.course_code = request.POST['course_code']
        course.duration = request.POST['duration']
        course.fee = request.POST['fee']
        course.save()

        return redirect('view_courses')

    return render(request, 'courses/edit_course.html', {'course': course})
def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('view_courses')