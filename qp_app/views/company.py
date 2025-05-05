from ..models import Company
from ..serializer import CompanySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_companies(request):
    companies = Company.objects.all()
    if not companies.exists():
        return Response({"message": "No companies found"}, status=204)
    
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_company(request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_company(request):
    company_id = request.data.get('id')
    if not company_id:
        return Response({"error": "Company ID required"}, status=400)
    
    try:
        company = Company.objects.get(id=company_id)
        company.delete()
        return Response({"message": "Company deleted successfully"})
    
    except Company.DoesNotExist:
        return Response({"error": "Company not found"}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_company(request):
    company_id = request.data.get('id')
    new_name = request.data.get('name')  
    
    if not company_id:
        return Response({"error": "Company ID required"}, status=400)
    if not new_name:
        return Response({"error": "Name field required"}, status=400)
    
    try:
        company = Company.objects.get(id=company_id)
        company.name = new_name
        company.save()
        return Response({"message": "Company updated successfully", "company": {"id": company.id, "name": company.name}})
    
    except Company.DoesNotExist:
        return Response({"error": "Company not found"}, status=404)
