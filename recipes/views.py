from django.shortcuts import render

# CLIENTE -> REQUEST | SERVIDOR -> RESPONSE
# HTTP Request
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Luiz'
    })   
    
def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Luiz'
    })