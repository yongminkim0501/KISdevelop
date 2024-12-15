from django.shortcuts import render

def board_user(request):
    return render(request, 'Board/board.html')