
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS=[
    ('PENDING','Pendente'),
    ('IN_PROGRESS','Em progresso'),
    ('DONE','Concluída')
    ]

    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    status=models.CharField(max_length=20,choices=STATUS,default='PENDING')
    priority=models.IntegerField(default=2)
    due_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
