from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Stock.ConnectKIS import *
from Stock.SearchStock import Stock
# 처음 만들어야 하는 view - token 로그인 여부 (로그인 시도 시 -> 로그인)
# nasdaq 주식 불러오기 버튼 - sql db에 저장하기, 100개
# 원하는 주식 (검색 - 코드, 접근 db)
# 해당 주식 (자신의 포트폴리오에 편입하기, model 새로 만들어야 함.)
# per, pbr, eps 등의 정보로 sql을 통해서 해당 정보 가져오기
# view에서 request 받은 후, 해당 관련 내용을 각 파일의 함수에 연결하는 코드 구현해야함.
# 1. token 로그인 기능 만들기
# 일단, accountManage에서 Stock 앱의 templates, token_connect.html 로 연결시킨 후,
# 해당 html 파일에서 버튼을 누르면 token 로그인을 시킨 후, token 로그인에 성공했습니다. 페이지 출력
# 해당 페이지에서 버튼을 누르면, nasdaq 주식 몇개를 가져오시겠습니까 여기서 개수를 누르면 해당 개수 만큼의 주식을 db에 저장
# 여기까지
def login_token(request):
    if request.method == 'POST':
        try:
            private_kis = PrivateKis()
            private_kis.connectKis()
            return JsonResponse({"success":True})
        except Exception as e:
            print('token 로그인에 실패했습니다.', e)

def connect_stock(request):
    if request.method == 'POST':
        try:
            stock = Stock()
            stock.connectStockToken(login_token.private_kis)
        except Exception as e:
            print('stock과 token 연결에 실패했습니다.')

def connect_token_page(request):
    return render(request, 'Stock/token_login.html')