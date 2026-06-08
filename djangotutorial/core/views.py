from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AIAuthor, NeuralNetworkType


def landing(request):
    return render(request, 'core/landing.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        if password != password_confirm:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El email ya está registrado')
            return redirect('register')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, 'Registro exitoso')
        return redirect('dashboard')
    
    return render(request, 'core/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Sesión iniciada correctamente')
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'core/login.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'Sesión cerrada correctamente')
    return redirect('landing')


@login_required
def dashboard(request):
    ai_authors = AIAuthor.objects.all()
    neural_network_types = NeuralNetworkType.objects.all()
    
    context = {
        'ai_authors': ai_authors,
        'neural_network_types': neural_network_types,
    }
    
    return render(request, 'core/dashboard.html', context)
