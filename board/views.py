from django.shortcuts import render
from .models import Board
from .forms import RegistForm
# Create your views here.
def index(request):
    board_list=Board.objects.all().order_by('-id')
    context = {'board_list':board_list}
    return render(request, 'board/index.html', context)
def regist(request):
    form = RegistForm()
    context = {'form':form}
    return render(request,'board/regist_form.html',context)