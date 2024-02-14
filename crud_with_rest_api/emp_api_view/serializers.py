from rest_framework import serializers
from .models import Employee

class EmployeeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        
class EmployeePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["email","fullname","emp_code","mobile","password"]
    # def validate(self, data):
    #     password = data.get('password')
    #     password2 = data.get('password2')
    #     if password != password2:
    #         raise serializers.ValidationError("Password and Confirm Password doesn't match")
    #     return data
    def create_user(self,data):
        password = data.pop('password2')
        instance = self.Meta.model(data)
        instance.set_password(password)  # Set password separately
        instance.save()
        return instance
    
class EmployeePutSerializer(serializers.Serializer):
    class Meta:
        model = Employee
        fields = ["email","fullname","emp_code","mobile","password","password2"]
        extra_kwargs={
            'password': {'write_only': True}
        }
    # def validate(self, data):
    #     password = data.get('password')
    #     password2 = data.get('password2')
    #     if password != password2:
    #         raise serializers.ValidationError("Password and Confirm Password doesn't match")
    #     return data
    def update(self, instance, validated_data):
        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.emp_code = validated_data.get('emp_code', instance.emp_code)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        return instance
