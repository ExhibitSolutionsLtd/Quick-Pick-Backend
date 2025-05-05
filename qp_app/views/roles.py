from ..models import Role
from ..serializer import RoleSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_roles(request):
    roles = Role.objects.all()
    if not roles.exists():
        return Response({"message": "No roles found"}, status=204)
    
    serializer = RoleSerializer(roles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_role(request):
    serializer = RoleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_role(request):
    role_id = request.data.get('id')
    if not role_id:
        return Response({"error": "Role ID required"}, status=400)
    
    try:
        role = Role.objects.get(id=role_id)
        role.delete()
        return Response({"message": "Role deleted successfully"})
    
    except Role.DoesNotExist:
        return Response({"error": "Role not found"}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_role(request):
    role_id = request.data.get('id')
    new_name = request.data.get('name')  
    
    if not role_id:
        return Response({"error": "Role ID required"}, status=400)
    if not new_name:
        return Response({"error": "Name field required"}, status=400)
    
    try:
        role = Role.objects.get(id=role_id)
        role.name = new_name
        role.save()
        return Response({"message": "Role updated successfully", "role": {"id": role.id, "name": role.name}})
    
    except Role.DoesNotExist:
        return Response({"error": "Role not found"}, status=404)