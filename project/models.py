from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.
class toDoList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    task = models.CharField(max_length=100,null=False,blank=False)
    remarks = models.TextField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=100,default='Incomplete')
    timeAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.task