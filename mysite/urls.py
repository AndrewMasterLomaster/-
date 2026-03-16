from django.contrib import admin
from django.urls import path
from mypage.views import home, secret_page, contacts, delete_message, signup
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('secret/', secret_page),
    path('contacts/', contacts),
    path('delete/<int:msg_id>/', delete_message, name='delete_msg'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'), # Добавил next_page
    path("signup/", signup, name = "signup"),
]
