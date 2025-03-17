from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from customer.models import Customer, CustomerAssignment, Agent
from users.models import CustomUser
from collectionplans.models import CashCollection,Scheme,CustomerScheme,CashCollectionEntry

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



class CustomerSchemeSerializer(serializers.ModelSerializer):
    customer_name = serializers.ReadOnlyField(source="customer.user.username") 
    scheme_name = serializers.ReadOnlyField(source="scheme.name")  

    class Meta:
        model = CustomerScheme
        fields = ['id', 'customer', 'customer_name', 'scheme', 'scheme_name', 'joined_date', 'amount_paid', 'status']



#     list_display = ("scheme", "start_date", "end_date")
#     filter_horizontal = ("customers",)  


class CashCollectionEntrySerializer(serializers.ModelSerializer):
    customer_scheme = CustomerSchemeSerializer(source="customer.enrolled_schemes", many=True, read_only=True)

    class Meta:
        model = CashCollectionEntry
        fields = '__all__'


