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
    return render(request, 'AccountManage/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # 로그인 후 이동할 페이지
        else:
            return render(request, 'AccountManage/login.html', {'error': '아이디 또는 비밀번호가 잘못되었습니다.'})
    return render(request, 'AccountManage/login.html')

@login_required
def home(request):
    return render(request, 'AccountManage/home.html', {'user': request.user})
#render 함수는 템플릿을 불러와서 html 페이지생성해 보여줌
#현재 url 유지한 채 템플릿만 렌더링
#템플릿에 데이터 context 를 전달할 수 있음.

def logout_user(request):
    logout(request)
    return redirect('login')
# 다른 url로 브라우저를 이동시킴
# 새로운 url로 실제 페이지 이동이 발생
# 브라우저의 주소창이 새로운 url로 변경

@login_required
def Move_Board(request):
    return redirect('Board:board')

@login_required
def Move_token(request): # stock의 앱으로 이동
    return redirect('Stock:stock')