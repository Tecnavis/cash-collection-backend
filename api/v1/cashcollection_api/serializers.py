from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from customer.models import Customer, CustomerAssignment, Agent
from users.models import CustomUser
from collectionplans.models import CashCollection,Scheme,CashCollectionEntry

class CashCollectionSerializer(ModelSerializer):
    class Meta:
        model = CashCollection
        fields = "__all__"

class SchemeSerializer(ModelSerializer):
    class Meta:
        model = Scheme
        fields = "__all__"        


class CashCollectionSerializer(serializers.ModelSerializer):
    scheme_name = serializers.ReadOnlyField(source="scheme.name") 
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), required=True)
    customer_name = serializers.ReadOnlyField(source="customer.user.username")  

    class Meta:
        model = CashCollection
        fields = "__all__"



class CashCollectionEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CashCollectionEntry
        fields = '__all__'

class CashCollectionSerializer(serializers.ModelSerializer):
    scheme_name = serializers.CharField(source='scheme.name', read_only=True)
    customer_name = serializers.SerializerMethodField()    
    scheme_total_amount = serializers.DecimalField(
        source="scheme.total_amount", max_digits=10, decimal_places=2, read_only=True
    )
    
    class Meta:
        model = CashCollection
        fields = ['id', 'scheme', 'scheme_name', 'customer', 'customer_name', 
                  'scheme_total_amount','start_date', 'end_date', 'created_at', 'updated_at']
    
    def get_customer_name(self, obj):
        if hasattr(obj.customer, 'user'):
            user = obj.customer.user
            return f"{user.first_name} {user.last_name}".strip() or user.username
        return "Unknown Customer"
