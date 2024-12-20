from django.urls import path
from . import views

app_name = 'Stock'

urlpatterns = [
    path('token-login/', views.connect_token_page, name='token_login'),
    path('login-token/', views.login_token, name='login_token'),
    path('connect-stock/', views.connect_stock, name='connect_stock'),
]