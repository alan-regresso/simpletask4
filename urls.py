
from django.urls import path
from . import views

urlpatterns=[
path('dashboard/',views.dashboard,name='dashboard'),

path('projects/',views.project_list,name='project_list'),
path('projects/create/',views.project_create,name='project_create'),
path('projects/<int:id>/delete/',views.project_delete,name='project_delete'),

path('tasks/',views.task_list,name='task_list'),
path('tasks/create/',views.task_create,name='task_create'),
path('tasks/<int:id>/complete/',views.task_complete,name='task_complete'),
]
