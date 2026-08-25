from django.contrib import admin
from .models import Task, Category
# Register your models here.


# admin for task table

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'completed',
        'priority',
        'category',
        'created_date',
        'due_date',
        'updated_at',
    )

    list_filter = (
        'completed',
        'priority',
        'category',
    )

    search_fields = (
        'title',
        'user',
        'created_date',
    )

    ordering = (
        'created_date',
    )

# admin for category table

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )
    search_fields = (
        'name',
    )
    ordering = (
        'name',
    )