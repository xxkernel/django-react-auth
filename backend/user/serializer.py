from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'age', 'gender', 'weight', 'height', 'fitness_goal')

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Adding custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['age'] = user.age
        token['gender'] = user.gender
        token['weight'] = str(user.weight)
        token['height'] = str(user.height)
        token['fitness_goal'] = user.fitness_goal
        return token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2', 'age', 'gender', 'weight', 'height', 'fitness_goal')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            age=validated_data['age'],
            gender=validated_data['gender'],
            weight=validated_data['weight'],
            height=validated_data['height'],
            fitness_goal=validated_data['fitness_goal']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user