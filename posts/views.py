from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView

from .models import Post


class CreatePostView(CreateView):
    pass
