from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout

def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')
        recipe_image = request.FILES.get('recipe_image')
        # print(recipe_name)
        # print(recipe_desc)
        # print(recipe_image)
        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_desc = recipe_desc,
            recipe_image = recipe_image,
        )
        return redirect('/recipes/')
    querryset = Recipe.objects.all()
    context = {'recipes':querryset}
    return render(request, 'recipe/recipes.html', context)

# def update_recipe(request, id):
#     querryset = Recipe.objects.get(id = id)
#     if request.method == 'POST':
#         data = request.POST
#         recipe_name = request.POST.get('recipe_name')
#         recipe_desc = request.POST.get('recipe_desc')
#         if request.FILES.get('recipe_image'):
#             recipe_image = request.FILES.get('recipe_image')
#         querryset.save()
#         return redirect('recipes')
#     context = {'recipe': querryset}
#     return render(request, 'update_recipe.html', context)
def update_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == "POST":
        recipe.recipe_name = request.POST['recipe_name']
        recipe.recipe_desc = request.POST['recipe_desc']
        if 'recipe_image' in request.FILES:
            recipe.recipe_image = request.FILES['recipe_image']
        recipe.save()
        return redirect('recipes')  # Or your main recipe list view
    return render(request, 'recipe/update_recipe.html', {'recipe': recipe})

def delete_recipe(request,id):
    querryset = Recipe.objects.get(id = id)
    querryset.delete()
    return redirect('/recipes/') 

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username")
            return redirect('/login/')
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/recipes/')
    return render(request , 'recipe/login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "Username allready exist")
            return redirect('/register/')
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.error(request, "Account created successfully")
        return redirect('/register/')
    return render(request, 'recipe/register.html')