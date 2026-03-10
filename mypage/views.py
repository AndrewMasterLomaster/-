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
    status = None # Сначала статуса нет
    
    if request.method == 'POST':
        name = request.POST.get('user_name')
        message = request.POST.get('user_message')
        # Сохраняем в базу (один раз!)
        ContactMessage.objects.create(name=name, message=message)
        status = 'СООБЩЕНИЕ СОХРАНЕНО В БАЗУ!'

    # ВАЖНО: Эти строки должны стоять БЕЗ лишних отступов (на уровне с "if")
    # Чтобы они срабатывали ПРИ ЛЮБОМ заходе на страницу
    all_messages = ContactMessage.objects.all()
    
    context = {
        'all_msgs': all_messages,
        'status': status
    }
    
    return render(request, 'contacts.html', context)



