from django.shortcuts import render
from django.http import HttpResponse

# CLIENTE -> REQUEST | SERVIDOR -> RESPONSE
# HTTP Request
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Luiz'
    })

def contato(request):
    return render(request, 'temp/temp.html')

def sobre(request):
    return HttpResponse('sobre')  

