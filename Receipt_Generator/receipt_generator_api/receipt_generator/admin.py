from django.contrib import admin
from .models import Item, Receipts

class ItemInline(admin.TabularInline):
    model = Item
    extra = 1

class ReceiptsAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'get_total_bill']
    readonly_fields = ['get_total_bill']

    def get_total_bill(self, obj):
        return obj.calculate_total()
    get_total_bill.short_description = 'Total Bill'

    inlines = [ItemInline]

admin.site.register(Receipts, ReceiptsAdmin)
admin.site.register(Item)

