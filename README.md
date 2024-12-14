# KISdeveloper

#로그인 기능 구현 
#setting.py 속 INSTALLED_APPS = [] 안에 내가 만든 APP이 추가 되어야 함(등록)
#views.py 에서 템플릿을 렌더링할 때는: return render(request, 'Stock/home.html') 이런 식으로 경로를 지정

my_private_peterlynch/           # 프로젝트 루트
├── Stock/                       # 앱 디렉토리
│   ├── templates/              # 템플릿 디렉토리
│   │   └── Stock/             # 앱 이름과 동일한 디렉토리
│   │       ├── home.html      # 템플릿 파일들
│   │       ├── login.html
│   │       └── register.html

#settings.pt 아래 부분 LOGIN_URL = 'login' # 로그인이 필요한 페이지 접근 시 리다이렉트 할 url
#LOGIN_REDIRECT_URL = 'home'

#views.py 에서 register_user 함수의 return redirect('login') 한 것이 저기로 간다고 생각하면 될 듯
#login_user 함수도 마찬가지

#views.py의 return redirect('login) 이 부분은 URL 패턴의 name을 참조
#urls.py에서 정의한 URL 패턴의 name 매개변수를 찾음.

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.home, name='home'),  # 홈 페이지
]

이 부분에 해당 
