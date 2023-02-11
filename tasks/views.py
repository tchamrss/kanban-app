from ast import Return
from time import strftime
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from tasks.models import Tasks, tasks_board

def index(request):
    '''
        this function leads to the homepage. This page is called when the user is authentificated
    '''
    if request.method == 'POST':
        print("received data " + request.POST['priority'])
        myTasksBoard = tasks_board.objects.get(id=1) 
        new_task = Tasks.objects.create(title=request.POST['title'], 
                                           description=request.POST['description'], 
                                           due_date=request.POST['dueDate'],
                                           priority=request.POST['priority'],
                                           task_board=myTasksBoard, 
                                           author=request.user)
        serialized_obj = serializers.serialize('json',[new_task])
        return JsonResponse(serialized_obj[1:-1], safe=False)        
    TasksCollections = Tasks.objects.filter(task_board__id=1)
    return render(request, 'tasks/index.html', {'tasks': TasksCollections})


def login_view(request):
    """_sumary_:this function leads to the login page. only a  registred user can be logged in 

    Args:
        request (_type_):Password and name required

    Returns:
        _type_: redirect to tasks when user is authenticated
    """
    if request.method == 'POST':
        user = authenticate(username = request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect('/tasks/')
        else:            
            return render(request,'auth/login.html', { 'wrongPassword': True})
    return render(request,'auth/login.html')


def register(request):
    """this function leads to the sign up page.

    Args:
        request (_type_): name, first name and password required

    Returns:
        _type_: _description_
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return render(request, 'tasks/index.html')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'auth/signup.html', context)



def logout_view(request):
    """log out function

    Args:
        request (_type_): this function log the user out

    Returns:
        _type_: _description_
    """
    logout(request)
    return render(request, 'auth/logout.html')   
