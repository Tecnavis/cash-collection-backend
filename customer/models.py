from django.db import models
from users.models import CustomUser

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="customer_profile")
    alternative_contact = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True, null=True)
    other_info = models.TextField(blank=True, null=True)
    
    created_by = models.ForeignKey(
        CustomUser, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='created_customers'
    )
    updated_by = models.ForeignKey(
        CustomUser, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='updated_customers'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class CustomerAssignment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="agent_assignments")
    agent = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="customer_assignments", 
                            limit_choices_to={'role': 'agent'})
    assigned_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    assigned_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="made_assignments")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.customer} assigned to {self.agent}"