from django.shortcuts import render, redirect
from .models import Person, CountChicken, Department, User
# Create your views here.
def main(request):
  return render(request, 'main.html')

def fur(request):
  
  return render(request, 'fur.html')

def fried(request):
  
  return render(request, 'fried.html')

def mix(request):
  
  return render(request, 'mix.html')

def rank(request):
  
  return render(request, 'rank.html')

def signup(request):
  
  departments = Department.objects.all()
  if request.method == 'POST':
    new_user = User.objects.create(
      username = request.POST['userid'],
      password = request.POST['userpw']
    )
    new_department = Department.objects.create(
      department_name = request.POST['department']
    ) 
    Person.objects.create(
      user = new_user,
      nickname = request.POST['usernickname'],
      department = new_department,
    )

    return redirect('login') 
  return render(request, 'signup.html', {'departments': departments})

def login(request):
  
  return render(request, 'login.html')