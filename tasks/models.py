from django.db import models

# Create your models here.

class TaskModel(models.Model):
    PRIORITY = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    ]
    STATUS = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    ]
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY ,null=True)
    status = models.CharField(max_length = 20, choices=STATUS, null=True)
    due_date = models.DateField(null=True)
    task_image = models.ImageField(upload_to='media/tasks',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}---{self.status}"
