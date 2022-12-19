from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from marketing.models import Lead
from marketing.serializers import LeadSerializer


@api_view(['GET','POST'])
def leads_list(request, format = None):
    """
    List all leads or create a new lead.
    """
    if request.method == 'GET':
        leads = Lead.objects.all()
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def lead_detail(request, id, format = None):
    """
    Retrieve, update or delete a lead.
    """
    try:
        lead = Lead.objects.get(id=id)
    except Lead.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LeadSerializer(lead)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LeadSerializer(lead, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        lead.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)