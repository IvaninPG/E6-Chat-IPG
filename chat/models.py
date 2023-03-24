from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Member(models.Model):
    memberUser = models.OneToOneField(User, on_delete=models.CASCADE)


class Chat(models.Model):
    name = models.CharField(max_length=64)
    member = models.ManyToManyField(Member)