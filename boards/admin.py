from django.contrib import admin

from .models import Category, Board

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "category",
        "created",
        "modified",
    ]
