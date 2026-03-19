from django.db import models
from django.contrib.auth.models import User

class ContactMessage(models.Model):
    # Связываем сообщение с Юзером. Если юзера удалят — его посты тоже (on_delete=CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)