from django.contrib import admin
from .models import Outflow


@admin.register(Outflow)
class AdminOutflow(admin.ModelAdmin):
    fields = [
        'product', 'quantity', 'description', 'created_at'
    ]
    search_fields = ('product__title',)
