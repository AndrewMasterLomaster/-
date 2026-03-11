from django.contrib import admin
from django.urls import path
from mypage.views import home, secret_rage, contacts, delete_message


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("secret/", secret_rage),
    path("contacts/", contacts),
    path("delete/<int:msg_id>/", delete_message, name="delete_msg"),
]
