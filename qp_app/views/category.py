from ..models import Category
from ..serializer import CategorySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_categories(request):
    categories = Category.objects.all()
    if not categories.exists():
        return Response({"message":"No categories found"}, status=204)
    
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_category(request):
    serializer = CategorySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_category(request):
    category_id = request.data.get('id')
    if not category_id:
        return Response({"error":"Category ID required"}, status=400)
    
    try:
        category = Category.objects.get(id=category_id)
        category.delete()
        return Response({"message":"Category deleted successfuly"})
    
    except Category.DoesNotExist:
        return Response({"error": "Category not found"}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_category(request):
    category_id = request.data.get('id')
    new_name = request.data.get('name')

    if not category_id:
        return Response({"error":"Category ID required"}, status=400)
    if not new_name:
        return Response({"error": "New category name required"}, status=400)
    
    try:
        category = Category.objects.get(id=category_id)
        category.name = new_name
        category.save()
        return Response({"message":"Category updated successfully"})
    except Category.DoesNotExist:
        return Response({"error":"Category not found"}, status=404)
