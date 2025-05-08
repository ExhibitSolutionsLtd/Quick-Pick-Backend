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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_customer(request):
    customer_id = request.data.get('id')
    if not customer_id:
        return Response({"error": "Customer ID required"}, status=400)
    
    try:
        customer = Customer.objects.get(id=customer_id)
        customer.delete()
        return Response({"message": "Customer deleted successfully"})
    
    except Customer.DoesNotExist:
        return Response({"error": "Customer not found"}, status=404)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_customer(request):
    customer_id = request.data.get('id')
    if not customer_id:
        return Response({'error': 'Customer ID is required.'}, status=400)

    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found.'}, status=400)
    
    serializer = CustomerSerializer(customer, data = request.data, partial=True)
    if serializer.is_valid():

        phone_number = serializer.validated_data.get('phone_number')
        if phone_number and Customer.objects.exclude(id=customer_id).filter(phone_number=phone_number).exists():
            return Response({'error':'Phone number already in use by another Customer'}, status=400)
        
        serializer.save()
        return Response({'message':'Customer updated successfully'}, status=200)
    return Response(serializer.errors, status=400)