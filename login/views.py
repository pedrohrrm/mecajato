from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
        return redirect(request.GET.get('next', 'clientes'))  # Redireciona para a página que estava tentando acessar
    else:
        form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login') 
    
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('/base')  # Redireciona para a página inicial
    else:
        form = UserCreationForm()
    return render(request, 'login/signup.html', {'form': form})


def base_view(request):
    # Redireciona o usuário para seu dashboard específico
    if is_admin(request.user):
        return redirect('admin_dashboard')
    elif is_teacher(request.user):
        return redirect('teacher_dashboard')
    elif is_student(request.user):
        return redirect('student_dashboard')
    else:
        messages.error(request, 'Você não tem acesso a esta página.')
        return redirect('login')