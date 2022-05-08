from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse

from .models import Board


def index(request):
    return TemplateResponse(request, "boards/index.html", {"board": board})

def board_detail(request, board_slug):
    board = get_object_or_404(Board, slug=board_slug)
    threads = board.threads.all()
    return TemplateResponse(request, "boards/board_detail.html", {"board": board})
