from .models import ContactMessage
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


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        message = request.POST.get('user_message')
        
        # ВОТ ОНА — МАГИЯ СОХРАНЕНИЯ В БАЗУ ✍️
        ContactMessage.objects.create(name=name, message=message)
        
        return render(request, 'contacts.html', {'status': 'СООБЩЕНИЕ СОХРАНЕНО В БАЗУ!'})

    return render(request, 'contacts.html')


