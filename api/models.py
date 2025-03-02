from django.db import models
import uuid
from django.utils.timezone import now

class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=now, editable=False)  # Correct name
    updated_at = models.DateTimeField(auto_now=True)
    expiration_date = models.DateField(null=True, blank=True)  # New field for expiration date

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    tin_number = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(default=now, editable=False)  # Correct name
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    transaction_code = models.CharField(max_length=50, unique=True, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    order_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(default=now, editable=False)  # Correct name
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.transaction_code:  # Generate only if not already set
            self.transaction_code = f"TXN{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.transaction_code


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_lines')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_lines')
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=now, editable=False)  # Correct name
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.order.transaction_code} - {self.product.name}"