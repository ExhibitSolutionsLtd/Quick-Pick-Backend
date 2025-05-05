from ..models import Customer
from ..serializer import CustomerSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_customers(request):
    customers = Customer.objects.all()
    if not customers.exists():
        return Response({"message":"No Customers found"}, status=204)
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


