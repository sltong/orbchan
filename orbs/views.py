from django.shortcuts import render
from django.template.response import TemplateResponse

from boards.models import Board


def index(request):
    boards = Board.objects.all()

    return TemplateResponse(request, "orbs/index.html", {
        "boards": boards
    })
