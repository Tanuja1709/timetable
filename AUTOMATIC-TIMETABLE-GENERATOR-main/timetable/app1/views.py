from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Course,Faculty,Section,TimetableEntry
from .forms import CourseForm , FacultyForm

# Create your views here.
def starting_page(request):
  return render(request , "app1/main.html")
def home_page(request):
  return render(request , "app1/home.html")
def admin1_page(request):
    return render(request, 'app1/admin1.html')
def fac_page(request):
    return render(request, 'app1/fac.html')
def faculty_page(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)

        if form.is_valid():
            if 'addfaculty' in request.POST:
                faculty = Faculty(
                    fid = form.cleaned_data['faculty_id'],
                    fname = form.cleaned_data['faculty_name']
                )
                faculty.save()
                return HttpResponseRedirect('faculty.html')
    else:
        form = FacultyForm()
        
    return render(request, 'app1/faculty.html',{
        "form" : form
    })

def student_page(request):
    return render(request, 'app1/student.html')

def course_page(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            if 'addcourse' in request.POST:
                course = Course(
                    cid=form.cleaned_data['course_id'],
                    cname=form.cleaned_data['course_name']
                )
                course.save()
                return HttpResponseRedirect('course.html')
    else:
        form = CourseForm()

    return render(request, 'app1/course.html', {"form": form})

        

def section_page(request):
    return render(request, 'app1/section.html')

def gentimetable_page(request):
    return render(request, 'app1/gentimetable.html')