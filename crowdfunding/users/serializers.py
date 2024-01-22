from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

# Create new users
#def create(self, validated_data):
    #new_user = CustomUser.objects.create_user(
        #username = validated_data["username"],
		#first_name = validated_data["first_name"],
		#last_name = validated_data["last_name"],
	    #email = validated_data["email"],
        #password = validated_data["password"]
    #)
    #new_user.save()
    #return new_user