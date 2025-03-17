from rest_framework import viewsets
from .serializers import CashCollectionSerializer, SchemeSerializer
from rest_framework.response import Response
from rest_framework import status
from collectionplans.models import CashCollection, Scheme
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes


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
