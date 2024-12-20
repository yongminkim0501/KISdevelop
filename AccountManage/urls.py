from django.urls import path
from . import views

urlpatterns = [
    path('Stock/', views.Move_token, name='move_token'), # stock 앱의 기능으로 이동
    path('Board/', views.Move_Board, name='move_board'), # board 앱의 기능으로 이동
    path('register/', views.register_user, name='register'), #유저 등록 기능으로 이동
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.home, name='home'),  # 홈 페이지
]