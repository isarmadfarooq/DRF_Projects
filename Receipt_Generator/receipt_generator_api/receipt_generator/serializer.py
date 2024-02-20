from rest_framework import serializers
from .models import Item, Receipts

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'quantity']

class ReceiptSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    total_bill = serializers.SerializerMethodField()

    class Meta:
        model = Receipts
        fields = ['id', 'items', 'created_at', 'total_bill']

    def get_total_bill(self, obj):
        return obj.calculate_total()
