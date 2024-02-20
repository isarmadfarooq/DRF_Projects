from django.db import models

class Receipts(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_total(self):
        if self.items.exists():
            total = sum(item.subtotal() for item in self.items.all())
            return total
        return 0

class Item(models.Model):
    receipt = models.ForeignKey(Receipts, related_name='items', on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def subtotal(self):
        return self.price * self.quantity


