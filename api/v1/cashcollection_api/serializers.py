from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from customer.models import Customer, CustomerAssignment, Agent
from users.models import CustomUser
from collectionplans.models import CashCollection,Scheme

class CashCollectionSerializer(ModelSerializer):
    class Meta:
        model = CashCollection
        fields = "__all__"

class SchemeSerializer(ModelSerializer):
    class Meta:
        model = Scheme
        fields = "__all__"        