from django.contrib import admin
from website.models import Dish, Nutrition


class NutritionInline(admin.StackedInline):
    model = Nutrition


class DishAdmin(admin.ModelAdmin):
    inlines = [NutritionInline,]


admin.site.register(Dish, DishAdmin)
