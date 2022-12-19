from celery import shared_task
import smtplib, ssl
from CRM.serializers import LeadSerializer as crm_leadser
import os

@shared_task
def send_email_on_qualified(request):
    serializer = crm_leadser(data=request.data)
    if not serializer.is_valid():
        return None
    if request.method == "PUT" and serializer.data['qualified']:
        context = ssl.create_default_context()
        try:
            email = os.environ.get('EMAIL_ADDRESS')
            password = os.environ.get('EMAIL_PASSWORD')
        except Exception as e:
            print('SEM EMAIL CADASTRADO PARA AUTOMAÇÃO')
            return None
        message = f"""\
            Ola, {serializer.data['name']}! Me chamo Ximira da Franq Open Banking.
            
            Vimos que se interessou por um de nossos produtos, gostaria de avancar para \
a proxima etapa de nossa parceria? Por favor acesse o link: \
http://localhost:8000/costumers \
e finalize o seu cadastro com a gente!
            """
        with smtplib.SMTP_SSL("smtp.gmail.com",port=465,context=context) as server:
            server.login(email, password)
            server.sendmail(email, serializer.data['email'], message)



