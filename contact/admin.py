from django.contrib import admin
from contact import models  #importaçao do model da classe contact

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = 'id', # escolha do campo para ordenação
    search_fields = 'id', 'first_name', 'last_name',  # adiciona um campo de pesquisa com esses atributos
    list_per_page = 5  # adiciona paginacao
    list_max_show_all = 200  # quantidade maxima que vc quer por pagina
    list_editable = 'first_name', 'last_name',  # campos para ediçao diretamente na pagina
    list_display_links = 'phone', 'id',  # campos que pode ser links