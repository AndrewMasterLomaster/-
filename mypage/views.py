from django.shortcuts import render

def home(request):
    context = {
        "username": "AndrewMasterLomaster",
        "status": "Admin",
    }
    return render(request, "home.html", context)



def secret_rage(request):
    my_projects = [
        'Создать личный блог на Django',
        'Написать To-Do List для школы',
        'Сделать сайт-визитку',
        'Взломать Пентагон '
    ]
    context = {
        "projects": my_projects
    }
    
    return render(request, "secret.html", context)
    
    
