from django.contrib import admin
from .models import Category, Task, User


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")