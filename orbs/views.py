from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, reverse
from django.template.response import TemplateResponse

from .forms import ThreadForm
from .models import Board, Thread, Post


def home(request):
    boards = Board.objects.all()

    return TemplateResponse(
        request,
        "home.html",
        {
            "boards": boards,
        },
    )


def boards(request):
    boards = Board.objects.all()

    return TemplateResponse(
        request,
        "boards.html",
        {
            "boards": boards,
        },
    )


def board(request, board_slug):
    boards = Board.objects.all()
    board = None
    threads = None
    form = ThreadForm()

    try:
        board = Board.objects.get(slug=board_slug)
        threads = board.threads.all()
    except Board.DoesNotExist:
        return Http404

    return TemplateResponse(
        request,
        "board.html",
        {
            "boards": boards,
            "board": board,
            "threads": threads,
            "form": form,
        },
    )


def create_thread(request, board_slug):
    board = get_object_or_404(Board, slug=board_slug)

    if request.method == "POST":
        form = ThreadForm(request.POST, request.FILES)

        if form.is_valid():
            new_thread = Thread.objects.create(
                board=board,
                subject=form.cleaned_data["subject"],
            )
            original_post = Post.objects.create(
                poster=request.user,
                thread=new_thread,
                text=form.cleaned_data["text"],
                image=form.cleaned_data["image"],
                file=form.cleaned_data["file"],
            )
            return HttpResponseRedirect(
                reverse("board", kwargs={"board_slug": board.slug})
            )

    else:
        form = ThreadForm()

    return TemplateResponse(
        request,
        "create_thread.html",
        {
            "board": board,
            "form": form,
        },
    )
