from celery import shared_task
import requests
from CRM.serializers import LeadSerializer as crm_leadser
from CRM.serializers import CostumerSerializer as crm_costumerser
from marketing.serializers import LeadSerializer as markt_leadser

@shared_task
def call_crm_leads_webhook(request):
    if request.method == "POST":
        serializer = crm_leadser(data=request.data)
        if serializer.is_valid():
            return requests.post('http://localhost:8000/crm/leads/', json=serializer.data)

@shared_task
def call_crm_costumer_webhook(request):
    if request.method == "POST":
        serializer = crm_costumerser(data=request.data)
        if serializer.is_valid():
            return requests.post('http://localhost:8000/crm/costumers/', json=serializer.data)

@shared_task
def call_marketing_leads_webhook(request):
    if request.method == "POST":
        serializer = markt_leadser(data=request.data)
        if serializer.is_valid():
            return requests.post('http://localhost:8000/marketing/leads/', json=serializer.data)
