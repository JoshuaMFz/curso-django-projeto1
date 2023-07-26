from django.shortcuts import render

# CLIENTE -> REQUEST | SERVIDOR -> RESPONSE
# HTTP Request
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Luiz'
    })


