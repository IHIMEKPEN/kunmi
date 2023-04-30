import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def health(request):
    return Response({
            'message': 'Hello Kunmi!'
        })

@api_view(['POST'])
def authRegister(request):
    data=json.loads(request.body)
    print(data)
    return Response({
            'message': 'signup successful',
            'data': data
        })

