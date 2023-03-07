
from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import RegistForm
# Create your views here.
def index(request):
    board_list=Board.objects.all().order_by('-id')
    context = {'board_list':board_list}
    return render(request, 'board/index.html', context)
def regist(request):
    if request.method== 'POST' :
        form = RegistForm(request.POST)
        print(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('board:index')
    else:
        form = RegistForm()
    context = {'form':form}
    return render(request,'board/regist_form.html',context)
def detail(request, pk):
    board_list = get_object_or_404(Board, id=pk)
    context = {'board_list':board_list}
    return render(request, 'board/detail.html',context)