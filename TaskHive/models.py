from django.db import models
from django.contrib.auth.models import User

class Taskdb(models.Model):
    title=models.CharField(max_length=50,blank=False)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here.
