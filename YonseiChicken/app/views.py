from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Person, CountChicken, Department, User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def main(request):

  return render(request, 'main.html')

@login_required(login_url="/login/")
def fur(request):
  
  return render(request, 'fur.html')

def fried(request):
  
  return render(request, 'fried.html')

def mix(request):
  
  return render(request, 'mix.html')

@login_required(login_url="/login/")
def rank(request):
  
  

  return render(request, 'rank.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['userid']
    password = request.POST['userpw']
    # print(username, password)
    user = auth.authenticate(username=username, password=password)
    # print(user)
    if user is not None:
      auth.login(request, user)
      return redirect('main')
    error = '아이디 또는 비밀번호가 틀립니다.'
    return render(request, 'login.html', {'error':error})
  return render(request, 'login.html')

def logout(request):
  auth.logout(request)
  return redirect('main')

def signup(request):
  departments = Department.objects.all()
  if request.method == 'POST':
    username = request.POST['userid']
    password = request.POST['userpw']

    exist_user = User.objects.filter(username=username)

    if exist_user:
      error = "이미 존재하는 아이디입니다."
      return render(request, 'signup.html', {'error':error, 'departments': departments})
    
    new_user = User.objects.create(
      username = username,
    )
    new_user.set_password(password)
    new_user.save()
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

def add_chicken(user, department):
  # 기존 치킨 수량 가져오기
  chicken = CountChicken.objects.get(user=user, department=department)
  temp = chicken.quantity
  temp += 1
  chicken.quantity = temp
  chicken.save()

def create_chicken(user, department):
  # 새로운 치킨 생성
  chicken = CountChicken.objects.create(user=user, department=department, quantity=1)

@csrf_exempt
def count(request):
    
    if request.method == 'POST':
      request_body = json.loads(request.body)
      # print('-------민기오빠세션', request_body)
    
   
      # print("count 시작")
    # 사용자와 부서 정보 가져오기
    
      user_id = request_body["id"]
      # print(user_id);
      # print(request.user, '받아온 것')

      person = Person.objects.get(pk = user_id)

      department = person.department  

      # 치킨 생성 또는 추가
      try:
          # print("치킨 있다")
          # 이미 치킨이 있는 경우
          add_chicken(person.user, department)
      except CountChicken.DoesNotExist:
          # print("치킨 없다")
          # 치킨이 없는 경우
          create_chicken(person.user, department)

      return HttpResponse(json.dumps({'success': True}))