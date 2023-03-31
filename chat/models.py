from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Member(models.Model):
    memberUser = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='icon/')


class Chat(models.Model):
    name = models.CharField(max_length=64)
    members = models.ManyToManyField(Member)

    def __init__(self):