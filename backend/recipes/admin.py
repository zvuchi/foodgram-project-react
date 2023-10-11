from django.contrib import admin

from .models import Ingredient, IngredientInRecipe, Recipe, Tag


class BaseAdminSettings(admin.ModelAdmin):
    empty_value_display = "-пусто-"
    list_filter = ("author", "name", "tags")


class TagAdmin(BaseAdminSettings):
    list_display = ("name", "color", "slug")
    list_display_links = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)


class IngredientAdmin(BaseAdminSettings):
    list_display = ("name", "measurement_unit")
    list_filter = ("name",)


class RecipeAdmin(BaseAdminSettings):
    list_display = ("name", "author", "added_in_favorites")
    list_display_links = ("name",)
    search_fields = ("name",)
    list_filter = ("author", "name", "tags")
    readonly_fields = ("added_in_favorites",)
    filter_horizontal = ("tags",)

    def added_in_favorites(self, obj):
        return obj.favorites.all().count()

    added_in_favorites.short_description = "Количество добавлений в избранное"


class IngredientInRecipeAdmin(admin.ModelAdmin):
    list_display = (
        "ingredient",
        "amount",
    )
    list_filter = ("ingredient",)


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientInRecipe, IngredientInRecipeAdmin)