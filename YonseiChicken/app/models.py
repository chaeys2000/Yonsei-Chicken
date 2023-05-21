from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Department(models.Model):
    # categories = (
    #     ('경영대학', '경영대학'),
    #     ('스마트모빌리티학부', '스마트모빌리티학부'),
    #     ('심리학부', '심리학부'),
    #     ('스마트보안학부', '스마트보안학부'),
    #     ('자유전공학부','자유전공학부'),
    #     ('보건과학대학', '보건과학대학'),
    #     ('미디어학부', '미디어학부'),
    #     ('국제대학', '국제대학'),
    #     ('디자인조형학부', '디자인조형학부'),
    #     ('정보대학', '정보대학'),
    #     ('간호대학', '간호대학'),
    #     ('사범대학', '사범대학'),
    #     ('의과대학', '의과대학'),
    #     ('공과대학', '공과대학'),
    #     ('이과대학', '이과대학'),
    #     ('정경대학', '정경대학'),
    #     ('생명과학대학', '생명과학대학'),
    #     ('문과대학', '문과대학')
    # )
    
    department_name = models.CharField(max_length=50,)
    def __str__(self):
        return self.department_name
    
class CountChicken(models.Model):

    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_chicken")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="Department_chicken")
    # quantity_of_department = models.PositiveIntegerField()

class Person(models.Model):
    # 추가 필드 정의
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_info")
    nickname = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, related_name="uers_department")
    count_chicken = models.ForeignKey(CountChicken, on_delete=models.CASCADE, null=True, related_name="uers_chickens")
    def __str__(self):
        return self.nickname