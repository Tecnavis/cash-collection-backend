from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from customer.models import Customer, CustomerAssignment
from users.models import CustomUser

class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=False, allow_null=True)
    updated_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Customer
        fields = "__all__"

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, "user"):
            validated_data["created_by"] = request.user
            validated_data["updated_by"] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, "user"):
            validated_data["updated_by"] = request.user
        return super().update(instance, validated_data)

class CustomerAssignmentSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    agent = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.filter(role="agent"))
    assigned_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=False, allow_null=True)

    class Meta:
        model = CustomerAssignment
        fields = "__all__"

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, "user"):
            validated_data["assigned_by"] = request.user
        return super().create(validated_data)
