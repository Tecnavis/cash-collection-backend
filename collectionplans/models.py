from django.db import models
from customer.models import Customer
from users.models import CustomUser


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
