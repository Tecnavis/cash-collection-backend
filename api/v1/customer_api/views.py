from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from customer.models import Customer
from .serializers import CustomerSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def customer_detail(request, id):
    """Retrieve details of a specific active customer."""
    customer = get_object_or_404(Customer, id=id, is_deleted=False)
    serializer = CustomerSerializer(customer)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def customer_create(request):
    """Create a new customer."""
    serializer = CustomerSerializer(data=request.data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def customer_update(request, id):
    """Update an existing customer."""
    customer = get_object_or_404(Customer, id=id, is_deleted=False)
    serializer = CustomerSerializer(customer, data=request.data, partial=True, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def customer_list(request):
    """Retrieve only active customers (users who are not deleted)."""
    customers = Customer.objects.filter(user__is_deleted=False)
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def customer_detail(request, id):
    """Retrieve details of a specific customer (if the user is not deleted)."""
    customer = get_object_or_404(Customer, id=id, user__is_deleted=False)
    serializer = CustomerSerializer(customer)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def customer_delete(request, id):
    """Soft delete a customer by setting user.is_deleted=True."""
    customer = get_object_or_404(Customer, id=id, user__is_deleted=False)
    customer.user.is_deleted = True
    customer.user.save()
    return Response({"message": "Customer soft deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def customer_restore(request, id):
    """Restore a soft-deleted customer by setting user.is_deleted=False."""
    customer = get_object_or_404(Customer, id=id, user__is_deleted=True)
    customer.user.is_deleted = False
    customer.user.save()
    return Response({"message": "Customer restored successfully"}, status=status.HTTP_200_OK)

