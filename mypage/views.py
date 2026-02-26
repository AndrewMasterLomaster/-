from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <body style="background-color: #28a745; color: white; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;">
            <div style="text-align: center;">
                <h1>Победа! Зеленый свет!</h1>
                <p>Я кожаный мешок, и я умею в дизайн через Django.</p>
                <br><br>
<a href="/secret/" style="color: yellow; font-weight: bold;">[ ВОЙТИ В СЕКРЕТНЫЙ РАЗДЕЛ ]</a>
            </div>
        </body>
    """)
    

def secret_rage(reuest):
    return HttpResponse("""
        <body style="background-color: black; color: #ff0000; font-family: 'Courier New', monospace; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;">
            <div style="text-align: center; border: 2px solid #ff0000; padding: 50px; box-shadow: 0 0 20px #ff0000;">
                <h1>ДОСТУП РАЗРЕШЕН</h1>
                <p>Добро пожаловать в секретный раздел, AndrewMasterLomaster.</p>
                <p>Тут будут твои будущие мега-проекты.</p>
                <a href="/" style="color: white; text-decoration: none; border-bottom: 1px dashed white;">Вернуться на главную</a>
            </div>
        </body>
    """)
    
