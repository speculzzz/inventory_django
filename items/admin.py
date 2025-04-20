from django.contrib import admin
from .models import Item, Inventory, Tag


class ModelItem(admin.ModelAdmin):
    list_display = ['name', 'weight']


admin.site.register(Item)
admin.site.register(Inventory)
admin.site.register(Tag)
