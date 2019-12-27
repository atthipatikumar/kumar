from django.shortcuts import render
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse

from .models import Details
from .serializers import DetailSerializers


@api_view(['GET', 'POST'])
def details_list(request, format=None):
    if request.method == 'GET':
        detail = Details.objects.all()
        serializer = DetailSerializers(detail, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DetailSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detail_view(request, pk, format=None):
    print(type(pk))
    try:
        if str.isnumeric(pk):
            detail = Details.objects.get(pk=pk)
        elif type(pk) == str:
            detail = Details.objects.get(Name=pk)
    except Details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DetailSerializers(detail)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if str.isnumeric(pk):
            detail = Details.objects.get(pk=pk)
            if request.data ['Name'] != '':

                serializer = DetailSerializers(detail, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

