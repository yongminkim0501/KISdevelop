from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Stock/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # 로그인 후 이동할 페이지
        else:
            return render(request, 'Stock/login.html', {'error': '아이디 또는 비밀번호가 잘못되었습니다.'})
    return render(request, 'Stock/login.html')

@login_required
def home(request):
    return render(request, 'Stock/home.html', {'user': request.user})

def logout_user(request):
    logout(request)
    return redirect('login')