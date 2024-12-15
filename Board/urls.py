from django.urls import path
from . import views

app_name = 'Board'

urlpatterns = [
    path('', views.board_user, name='board'),
]