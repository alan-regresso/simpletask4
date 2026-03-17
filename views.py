
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project,Task
from .forms import ProjectForm,TaskForm

@login_required
def dashboard(request):
    projects=Project.objects.filter(owner=request.user)
    tasks=Task.objects.filter(project__owner=request.user)
    urgent=tasks.order_by('due_date')[:5]

    return render(request,'dashboard.html',{
    'total_projects':projects.count(),
    'pending_tasks':tasks.count(),
    'urgent_tasks':urgent
    })

@login_required
def project_list(request):
    projects=Project.objects.filter(owner=request.user)
    return render(request,'projects/list.html',{'projects':projects})

@login_required
def project_create(request):
    form=ProjectForm(request.POST or None)
    if form.is_valid():
        project=form.save(commit=False)
        project.owner=request.user
        project.save()
        return redirect('project_list')
    return render(request,'projects/form.html',{'form':form})

@login_required
def project_delete(request,id):
    project=get_object_or_404(Project,id=id,owner=request.user)
    project.delete()
    return redirect('project_list')

@login_required
def task_list(request):
    tasks=Task.objects.filter(project__owner=request.user)
    return render(request,'tasks/list.html',{'tasks':tasks})

@login_required
def task_create(request):
    form=TaskForm(request.POST or None)
    form.fields['project'].queryset=Project.objects.filter(owner=request.user)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request,'tasks/form.html',{'form':form})

@login_required
def task_complete(request,id):
    task=get_object_or_404(Task,id=id,project__owner=request.user)
    if request.method=='POST':
        task.status='DONE'
        task.save()
    return redirect('task_list')
