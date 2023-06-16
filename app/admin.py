from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    pass