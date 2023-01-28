from django.contrib import admin
from .models import Tree
# Register your models here.


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    ordering = ('menu_name',)
