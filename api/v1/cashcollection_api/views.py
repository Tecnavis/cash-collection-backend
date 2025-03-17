from rest_framework import viewsets
from .serializers import CashCollectionSerializer, SchemeSerializer,CashCollectionSerializer,CustomerSchemeSerializer,CashCollectionEntrySerializer
from rest_framework.response import Response
from rest_framework import status
from collectionplans.models import CashCollection, Scheme
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes
from customer.models import Customer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def scheme_list(request):
    """Retrieve all schemes."""
    schemes = Scheme.objects.all()
    serializer = SchemeSerializer(schemes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def scheme_create(request):
    """Create a new scheme."""
    serializer = SchemeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def enroll_customer_in_scheme(request):
    """Enrolls a customer in a selected scheme (Creates CashCollection)."""
   
    if not request.data.get("customer") or not request.data.get("scheme"):
        return Response({"error": "Customer and Scheme are required"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        customer = Customer.objects.get(id=request.data["customer"])
    except Customer.DoesNotExist:
        return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
    try:
        scheme = Scheme.objects.get(id=request.data["scheme"])
    except Scheme.DoesNotExist:
        return Response({"error": "Scheme not found"}, status=status.HTTP_404_NOT_FOUND)
    
    existing_entry = CashCollection.objects.filter(scheme=scheme, customer=customer).exists()
    if existing_entry:
        return Response({"error": "Customer is already enrolled in this scheme"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Prepare data for serializer
    data = request.data.copy()
    
    serializer = CashCollectionSerializer(data=data)
    if serializer.is_valid():
        # Pass customer and scheme directly, don't try to add customer afterwards
        cash_collection = serializer.save(
            created_by=request.user,
            customer=customer,
            scheme=scheme
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def enroll_customer_in_scheme(request):
#     """Enrolls a customer in a selected scheme (Creates CashCollection)."""
   
#     serializer = CashCollectionSerializer(data=request.data)
   
#     if not request.data.get("customers") or not request.data.get("scheme"):
#         return Response({"error": "Customer and Scheme are required"}, status=status.HTTP_400_BAD_REQUEST)
#     try:
#         customer = Customer.objects.get(id=request.data["customers"])
#     except Customer.DoesNotExist:
#         return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
#     try:
#         scheme = Scheme.objects.get(id=request.data["scheme"])
#     except Scheme.DoesNotExist:
#         return Response({"error": "Scheme not found"}, status=status.HTTP_404_NOT_FOUND)
#     existing_entry = CashCollection.objects.filter(scheme=scheme, customers=customer).exists()
#     if existing_entry:
#         return Response({"error": "Customer is already enrolled in this scheme"}, status=status.HTTP_400_BAD_REQUEST)
#     if serializer.is_valid():
#         cash_collection = serializer.save(created_by=request.user)
#         cash_collection.customers.add(customer)  
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def enroll_customer_in_scheme(request):
#     """Enrolls a customer in a selected scheme (Creates CashCollection)."""
    
#     serializer = CashCollectionSerializer(data=request.data)
    
#     if not request.data.get("customer") or not request.data.get("scheme"):
#         return Response({"error": "Customer and Scheme are required"}, status=status.HTTP_400_BAD_REQUEST)

#     try:
#         customer = Customer.objects.get(id=request.data["customer"])
#     except Customer.DoesNotExist:
#         return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

#     try:
#         scheme = Scheme.objects.get(id=request.data["scheme"])
#     except Scheme.DoesNotExist:
#         return Response({"error": "Scheme not found"}, status=status.HTTP_404_NOT_FOUND)

#     existing_entry = CashCollection.objects.filter(scheme=scheme, customers=customer).exists()
#     if existing_entry:
#         return Response({"error": "Customer is already enrolled in this scheme"}, status=status.HTTP_400_BAD_REQUEST)

#     if serializer.is_valid():
#         cash_collection = serializer.save(created_by=request.user)
#         cash_collection.customers.add(customer)  

#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cash_collection_create(request):
    data = request.data
    serializer = CashCollectionEntrySerializer(data=data)

    if serializer.is_valid():
        serializer.save(created_by=request.user, updated_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)