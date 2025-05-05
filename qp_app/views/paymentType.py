from ..models import PaymentType
from ..serializer import PaymentTypeSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_payment_types(request):
    payments = PaymentType.objects.all()
    if not payments.exists():
        return Response({"message": "No payment types found"}, status=204)
    
    serializer = PaymentTypeSerializer(payments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_payment_type(request):
    serializer = PaymentTypeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_payment_type(request):
    payment_type_id = request.data.get('id')
    if not payment_type_id:
        return Response({"error": "Payment type ID required"}, status=400)
    
    try:
        payment_type = PaymentType.objects.get(id=payment_type_id)
        payment_type.delete()
        return Response({"message": "Payment type deleted successfully"})
    
    except PaymentType.DoesNotExist:
        return Response({"error": "Payment type not found"}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_payment_type(request):
    payment_type_id = request.data.get('id')
    new_name = request.data.get('name')
    
    if not payment_type_id:
        return Response({"error": "Payment type ID required"}, status=400)
    if not new_name:
        return Response({"error": "Name field required"}, status=400)
    
    try:
        payment_type = PaymentType.objects.get(id=payment_type_id)
        payment_type.name = new_name
        payment_type.save()
        return Response({"message": "Payment type updated successfully", "payment_type": {"id": payment_type.id, "name": payment_type.name}})
    
    except PaymentType.DoesNotExist:
        return Response({"error": "Payment type not found"}, status=404)
