from django.shortcuts import render, get_object_or_404, redirect
from .models import Board
from django.contrib.auth.models import User
from .models import Board, Topic, Post
from django.http import Http404, HttpResponse
from .forms import NewTopicForm, MemberModelForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

def home(request):
    boards = Board.objects.all()
    return render(request, 'boards/home.html',{'boards': boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'boards/topics.html', {'board': board})

@login_required
def new_topic(request,pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()

    if request.method == 'POST':
        form = NewTopicForm(request.POST)

        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)
    else:
        form = NewTopicForm()

    return render(request, 'boards/new_topic.html', {'board': board, 'form': form})



def e1_index(request):
    context = {
        'form': MemberModelForm(),
    }
    return render(request, 'boards/e1/index.html', context)

@require_POST
def e1_save(request):
    form = MemberModelForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('boards:e1_index')

    context = {
        'form': form,
    }
    return render(request, 'boards/e1/index.html', context)
