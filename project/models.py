from django.db import models
import uuid

# Create your models here.
class toDoList(models.Model):
    task = models.CharField(max_length=100,null=False,blank=False)
    remarks = models.TextField(max_length=100,null=True,blank=True)
    timeAdded = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self) :
        return self.task