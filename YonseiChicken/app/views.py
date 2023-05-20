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

def singup(request):
  
  return render(request, 'login.html')
