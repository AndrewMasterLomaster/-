from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <body style="background-color: #28a745; color: white; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;">
            <div style="text-align: center;">
                <h1>Победа! Зеленый свет!</h1>
                <p>Я кожаный мешок, и я умею в дизайн через Django.</p>
            </div>
        </body>
    """) # И эти скобки — ПИШИ САМ
    
