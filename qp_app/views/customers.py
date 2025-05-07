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

    full_name = request.data.get('full_name')
    phone_number = request.data.get('phone_number')
    total_purchases = request.data.get('total_purchases')

    if full_name:
        customer.full_name = full_name
    if phone_number:
        if Customer.objects.exclude(id=customer_id).filter(phone_number=phone_number).exists():
            return Response({'error': 'Phone number already in use by another customer.'}, status=400)
        customer.phone_number = phone_number
    if total_purchases is not None:
        try:
            customer.total_purchases = int(total_purchases)
        except ValueError:
            return Response({'error': 'Total purchases must be an integer.'}, status=400)

    customer.save()
    return Response({'message': 'Customer updated successfully.'}, status=200)



