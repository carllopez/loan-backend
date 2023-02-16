from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Record
from .operations import addition, subtract, multiplication, division, square_root, random_string
from .serializers import RecordSerializer, StandardNumericSerializer, SingleNumericSerializer, EnmptySerializer


class RecordList(generics.ListCreateAPIView):
    """
    List all `Record` objects, for a given user
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def list(self, request, pk=None):
        queryset = self.get_queryset().filter(user=pk)
        serializer = RecordSerializer(queryset, many=True)
        return Response(serializer.data)


class OperationRequest(APIView):
    """
    Choose an operation and return the right response,
    if parameters are well formed and operation is valid.
    """

    def post(self, request, format=None):
        operation = request.data.get('operation', None)
        if not operation:
            return Response({'error': 'Operation is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Standard operations
        if operation in [1, 2, 3, 4]:
            serializer = StandardNumericSerializer(data=request.data)
        # Square root
        elif operation == 5:
            serializer = SingleNumericSerializer(data=request.data)
        # Anything else
        else:
            serializer = EnmptySerializer(data=request.data)

        if not serializer.is_valid():
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        match operation:
            case 1:
                result = addition(serializer.data['operand_a'], serializer.data['operand_b'])
            case 2:
                result = subtract(serializer.data['operand_a'], serializer.data['operand_b'])
            case 3:
                result = multiplication(serializer.data['operand_a'], serializer.data['operand_b'])
            case 4:
                result = division(serializer.data['operand_a'], serializer.data['operand_b'])
            case 5:
                result = square_root(serializer.data['operand_a'])
            # 6 or any other value will default to random string
            case _:
                result = random_string()

        response_data = {'result': result}

        return Response(response_data, status=status.HTTP_200_OK)
