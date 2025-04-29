from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from ..serializer import UserRegistrationSerializer
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error)

