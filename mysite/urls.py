from django.contrib import admin
from django.urls import path
from mypage.views import home, secret_rage, contacts


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("secret/", secret_rage),
    path("contacts/", contacts)
]
