from django.contrib import admin
from contact import models  #importaçao do model da classe contact

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    ...
