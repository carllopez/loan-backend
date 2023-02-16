from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Operation, Record


# Models related serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation


class RecordSerializer(serializers.ModelSerializer):
    operation = serializers.SerializerMethodField()

    class Meta:
        model = Record
        fields = ['operation', 'user', 'amount', 'user_balance', 'operation_response', 'date']

    def get_operation(self, obj):
        return obj.operation.get_type_display()


# Incoming operations related serializers

class StandardNumericSerializer(serializers.Serializer):
    operation = serializers.IntegerField(required=True)
    operand_a = serializers.IntegerField(required=True)
    operand_b = serializers.IntegerField(required=True)


class SingleNumericSerializer(serializers.Serializer):
    operation = serializers.IntegerField(required=True)
    operand_a = serializers.IntegerField(required=True)


class EnmptySerializer(serializers.Serializer):
    operation = serializers.IntegerField(required=True)
