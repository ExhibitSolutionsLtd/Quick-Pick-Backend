from django.shortcuts import render
from django.contrib.auth.models import User
from ..models import ExpenseModel
from ..serializer import ExpenseSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_ExpenseAdded(request):
    user = request.user 
    products = ExpenseModel.objects.filter(added_by=user)
    if not products.exists():
        return Response({"message": "No expenses found."}, status=204)
    
    serializer = ExpenseSerializer(products, many=True)
    return Response(serializer.data)

