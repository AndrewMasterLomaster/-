from .models import ContactMessage
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required # ЭТОТ ЗАМОК НЕ ПУСТИТ АНОНИМОВ 🔐
def delete_message(reuest, msg_id):
    msg = Contactmessage.objects.get(id=msg_id)
    msg.delete()
    return  redirect("/contacts/")

def home(request):
    context = {
        "username": "AndrewMasterLomaster",
        "status": "Admin",
    }
    return render(request, "home.html", context)



def secret_page(request):
    # Твой список проектов, который мы делали раньше
    my_projects = ['Взлом Пентагона', 'Сайт для кота', 'Секретка']
    context = {'projects': my_projects}
    return render(request, 'secret.html', context)



def contacts(request):
    status = None
    
    # 1. Сначала ПРИЕМ (сохранение) нового сообщения
    if request.method == 'POST':
        name = request.POST.get('user_name')
        message = request.POST.get('user_message')
        ContactMessage.objects.create(name=name, message=message)
        status = 'СООБЩЕНИЕ СОХРАНЕНО В БАЗУ!'

    # 2. Теперь ПОДГОТОВКА СПИСКА (всех сообщений)
    # Сначала берем всё и сортируем (самые новые сверху)
    all_messages = ContactMessage.objects.all().order_by('-created_at')

    # 3. МАГИЯ ФИЛЬТРАЦИИ (Поиск)
    query = request.GET.get('search') # Берем текст из поля поиска
    if query:
        # Оставляем только те, в которых имя СОДЕРЖИТ текст из поиска
        all_messages = all_messages.filter(name__icontains=query)

    # 4. ОТПРАВЛЯЕМ В ШАБЛОН
    context = {
        'all_msgs': all_messages,
        'status': status
    }
    return render(request, 'contacts.html', context)


def delete_message(request, msg_id):
    # Находим сообщение по его номеру (ID)
    msg = ContactMessage.objects.get(id=msg_id)
      # Удаляем его из базы
    msg.delete()
       # Возвращаемся обратно на страницу контактов
    return redirect("/contacts/")



