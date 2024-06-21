'''
Este modulo serve para configurar a exibicao das
 tabelas na pagina admin do Django
'''

from django.contrib import admin
from contact import models

# Register your models here.

# aprender especificamente sobre decorators


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = '-id',
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_max_show_all = 100
    list_per_page = 10
    list_display_link = 'phone', 'first_name', 'last_name'


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
