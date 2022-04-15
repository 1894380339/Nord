# from rest_framework import serializers
# from .models import User,Task

# TO DO 1
# class Singup_serializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
#     class Meta:
#         model = User
#         fields = ['username','email','password','password2']
#         extract_kwargs = {
#             'password':{'write_only':True}
#             }
#     def save(self):
#         acount = User(
#             username = self.validated_data['username'],
#             email = self.validated_data['email'],  
#                 )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']
#         if password!= password2:
#             raise serializers.ValidationError({'password':'passwords must match.'})
#         else:
#             acount.set_password = password
#             acount.save()
#             return acount