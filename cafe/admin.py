from django.contrib import admin

from cafe.models import Category,Menu,Order,Payment

@admin.register(Menu)
class CafeAdmin(admin.ModelAdmin):
    list_display = ("menu_name","price",)

