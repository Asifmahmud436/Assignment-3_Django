from django.db import models
from category.models import Category

class Task(models.Model):
    taskTitle = models.CharField(max_length=20)
    taskDescription = models.CharField(max_length=50)
    task_assign_date = models.DateField()
    category = models.ManyToManyField(Category)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.taskTitle

