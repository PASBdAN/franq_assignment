from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from website.models import Lead, Costumer
from website.serializers import LeadSerializer, CostumerSerializer
from website.tasks import call_crm_leads_webhook, call_marketing_leads_webhook, call_crm_costumer_webhook


@api_view(['GET','POST'])
def leads_list(request, format = None):
    """
    List all leads or create a new lead.
    """
    print(request)
    print(type(request))
    if request.method == 'GET':
        leads = Lead.objects.all()
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            call_crm_leads_webhook(request)
            call_marketing_leads_webhook(request)

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

@api_view(['GET','POST'])
def costumers_list(request, format = None):
    """
    List all leads or create a new lead.
    """
    if request.method == 'GET':
        leads = Costumer.objects.all()
        serializer = CostumerSerializer(leads, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CostumerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            call_crm_costumer_webhook(request)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def costumer_detail(request, id, format = None):
    """
    Retrieve, update or delete a costumer.
    """
    try:
        costumer = Costumer.objects.get(id=id)
    except Costumer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CostumerSerializer(costumer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CostumerSerializer(costumer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        costumer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)