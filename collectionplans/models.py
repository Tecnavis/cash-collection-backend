from django.db import models
from customer.models import Customer
from users.models import CustomUser
from financials.models import Transaction


class CollectionFrequencyChoices:
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    CUSTOM = "custom"

    CHOICES = [
        (DAILY, "Daily"),
        (WEEKLY, "Weekly"),
        (MONTHLY, "Monthly"),
        (CUSTOM, "Custom"),
    ]

class CashCollectionScheme(models.Model):
    scheme_name = models.CharField(max_length=255, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    collection_frequency = models.CharField(max_length=10, choices=CollectionFrequencyChoices.CHOICES)
    installment_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    customers = models.ManyToManyField(Customer, related_name="assigned_schemes")

    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="created_schemes")
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="updated_schemes")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.scheme_name


class CashFlow(models.Model):
    balance_type = models.CharField(max_length=50, choices=[("bank", "Bank"), ("hand_cash", "Hand Cash")])
    total_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return f"{self.balance_type} - {self.total_balance}"

class Refund(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name="refunds")  # Add this field
    amount_refunded = models.DecimalField(max_digits=12, decimal_places=2)
    approved_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="approved_refunds")
    refund_date = models.DateTimeField(auto_now_add=True)

