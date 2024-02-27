from django.shortcuts import render
from .models import Tasktable
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def task_manage(request):
    tasks = Tasktable.objects.all()
    return render(request, 'task_manage.html', {'tasks': tasks})

@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        print(1)
        taskid = request.POST.get('taskid')
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        completed = request.POST.get('completed')
        print(taskid)
        if taskid == "":
           
            task = Tasktable(title=title, description=description, due_date=due_date, priority=priority,
                         completed=completed)
            
        else:
             task = Tasktable(id=taskid,title=title, description=description, due_date=due_date, priority=priority,
                         completed=completed)
        task.save()
             

        task_value = Tasktable.objects.values()
        task_data = list(task_value)
        return JsonResponse({"status": "Saved","task_data": task_data})
    else:
        return JsonResponse({"status":"not saved"})
    
@csrf_exempt
def delete_task(request):
    if request.method == "POST":
        id = request.POST.get("taskid")
        task = Tasktable.objects.get(id=id)
        task.delete()
        return JsonResponse({"status":1})
    else:
        return JsonResponse({"status":0})

@csrf_exempt
def update_task(request):
    if request.method == "POST":
        id = request.POST.get("taskid")
        task = Tasktable.objects.get(id=id)
        task_data = {"id":task.id,"title":task.title,"description":task.description,
        "completed":task.completed,"due_date":task.due_date.strftime('%Y-%m-%dT%H:%M'),
        "priority":task.priority}
        return JsonResponse(task_data)
    else:
        return JsonResponse({"status":"Task not found"})
