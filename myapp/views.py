from django.shortcuts import render,redirect
from myapp.models import Student,College
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


# Create your views here.


def add_people(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    mobile_number = request.POST.get('mobile_number')
    age = request.POST.get('age')
    college_id = request.POST.get('college')

    college =  College.objects.get(id=college_id)
    Student.objects.create(
      name=name,
      mobile_number=mobile_number,
      age=age,
      college = college
    )
    return redirect('Search')
  colleges=College.objects.all()
  return render(request,'Add.html',{'colleges':colleges})

def delete_people(request,pk):
  student = get_object_or_404(Student, pk=pk)
  student.delete()
  return redirect('Search')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, College

def update_person(request, pk):
    # Fetch the student or return a 404
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        # Get data from form submission
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        age = request.POST.get('age')
        college_id = request.POST.get('college')

        # Validation: Ensure required fields are filled
        if not (name and mobile_number and age and college_id):
            colleges = College.objects.all()
            return render(request, 'Update.html', {
                'student': student,
                'colleges': colleges,
                'error': 'All fields are required.'
            })

        try:
            # Fetch the selected college
            colleges = College.objects.get(id=college_id)
            print(colleges)

            # Update the student object
            student.name = name
            student.mobile_number = mobile_number
            student.age = age
            student.college = colleges
            student.save()

            # Redirect to the list or detail page
            return redirect('Search')  # Replace 'students_list' with the desired URL
        except College.DoesNotExist:
            colleges = College.objects.all()
            return render(request, 'update_person.html', {
                'student': student,
                'colleges': colleges,
                'error': 'Selected college does not exist.'
            })

    # For GET request, render the update form
    colleges = College.objects.all()
    return render(request, 'update_person.html', {
        'student': student,
        'colleges': colleges
    })


def search_page(request):
  students = Student.objects.all()
  search = request.GET.get('search')
  age = request.GET.get('age')

  if search:
    students = students.filter(
      Q(name__icontains = search)|
       Q(college__college_name__icontains = search)|
        Q(mobile_number__startswith = search)
      )
  if age:
    if age == "1":
      students = students.filter(age__gte=18 , age__lte=20).order_by('age')
    if age == "2":
      students = students.filter(age__gte=20 , age__lte=23).order_by('age')
    if age == "3":
       students = students.filter(age__gte=25).order_by('age')


  context={'students': students}

  return render(request,'search.html',context)


# def index(request):
#      data={
#         "status":True,
#         "message":"django-server"
#      }
#      return JsonResponse(data)