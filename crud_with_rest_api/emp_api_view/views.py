from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication 
from .models import Employee
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken 
from .serializers import EmployeeGetSerializer,EmployeePostSerializer,EmployeePutSerializer
from rest_framework import status

def get_tokens_for_emp(emp):
    refresh = RefreshToken.for_user(emp)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
# Create your views here.
class EmployeeGetView(APIView):
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        # many=True is used when in drf we want to serialize a queryset containing multiple objects, rather than just a single object.
        serializer = EmployeeGetSerializer(employees, many=True)
        return Response({"employees": serializer.data})

class EmployeeCreateView(APIView):
        
    def post(self, request, *args, **kwargs):
        serializer=EmployeePostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            emp=serializer.save()
            token=get_tokens_for_emp(emp)
            return Response({"token":token,"msg":"employee is successfully registered"})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)  
    
class EmployeeTokenCreationView(APIView):

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return None
    def get(self, request, pk, *args, **kwargs):
        emp = self.get_object(pk)
        if emp:
            serializer = EmployeeGetSerializer(emp)
            token=get_tokens_for_emp(emp)
            return Response({"data":serializer.data,"token":token})
        return Response({"msg": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
    
class EmployeeRetreiveUpdateView(APIView):
        
    permission_classes = [IsAuthenticated] 
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return None
    def get(self, request, pk, *args, **kwargs):
        emp = self.get_object(pk)
        if emp:
            serializer = EmployeeGetSerializer(emp)
            token=get_tokens_for_emp(emp)
            return Response({"data":serializer.data,"token":token})
        return Response({"msg": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
    def put(self, request, pk, *args, **kwargs):
        emp = self.get_object(pk)
        if emp:
            serializer = EmployeePutSerializer(data=request.data, context = {'emp':request.user})
            if serializer.is_valid(raise_exception=True):
                return Response({'msg':'Employee info is successfully updated'}, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({"msg": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request,pk, *args, **kwargs):
        emp = self.get_object(pk)
        if emp:
            emp.delete()
            return Response({'msg':'Employee deleted, and now, no longer exists in database'}, status = status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)
            
