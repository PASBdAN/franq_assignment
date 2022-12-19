# DESAFIO TÉCNICO - ENGENHEIRO DE AUTOMAÇÃO E INTEGRAÇÃO

### O foco principal deste desafio é demonstrar a capacidade de implementar uma stack de integração de dados entre sistemas distribuídos com um mecanismo de mensageria para processamento em background. Será utilizada a stack Django (client) com Celery (task queue) e Redis (broker), e a integração dos dados será dada com a automação de requisições para os endpoints dos sistemas via tasks. Para fins de praticidade no deploy da stack, será utilizado docker-compose para montar toda a infraestrutura, que incluirá um banco de dados postgres e uma interface de monitoramento das tasks e workers do Celery com Flower.

### Abstraiu-se do desafio 3 sistemas distintos:
 - Website: Será representado como um app "website" no django com um endpoint para simular o POST do forms do lead.
 - Sistema de Automação de Marketing Digital: Será representado como um app "marketing" no django com um endpoint GET para inserção dos leads via task.
 - CRM: Será representado como um app "CRM" no django com varios endpoints para simular o fluxo de qualificação de leads, envio de forms e cadastro de clientes efetivos.

## BUILD:

 - docker-compose build
 - docker compose up

## ENDPOINTS:
 - /leads/ [GET, POST]
 - /leads/<int:id>/ [GET, PUT, DELETE]
 - /marketing/leads/ [GET, POST]
 - /marketing/leads/<int:id>/ [GET, PUT, DELETE]
 - /crm/leads/ [GET, POST]
 - /crm/leads/<int:id>/ [GET, PUT, DELETE]
 - /costumers/ [GET, POST]
 - /costumers/<int:id>/ [GET, PUT, DELETE]
 - /crm/costumers/ [GET, POST]
 - /crm/costumers/<int:id>/ [GET, PUT, DELETE]

## FLUXO DOS DADOS:
  - 1  : Website lead forms POST
  - 1.1: Digital marketing lead POST (automated with task)
  - 1.2: CRM lead POST (automated with task)
  - 2  : CRM lead PUT qualified = true 
  - 2.1: Send email to lead (automated with task)
  - 3  : Website costumer forms POST
  - 3.1: CRM costumer POST (automated with task)

## OBSERVAÇÕES:
 * 1 - A task de envio de email ao qualificar o lead no CRM só funcionará se for especificado no arquivo .env as variáveis: EMAIL_ADDRESS e EMAIL_PASSWORD, credenciais obrigatoriamente de uma conta do gmail.
 * 2 - É possível também simular o fluxo pela interface web do django restframework, acessando as urls dos endpoints via o navegador.

## REFERENCIAS:
 - Monitoring a Dockerized Celery Cluster with Flower: https://www.distributedpython.com/2018/10/13/flower-docker/
 - Dockerizing Django with Postgres, Redis and Celery: https://soshace.com/dockerizing-django-with-postgres-redis-and-celery/
 - Message Queues with Celery, Redis, and Django: https://tamerlan.dev/message-queues-with-celery-redis-and-django/
 - Asynchronous Tasks with Celery + Redis in Django: https://melvinkoh.me/asynchronous-tasks-with-celery-redis-in-django-cjye4tgaw000luns1ngthq609
 - Django Rest Framework Docs: https://www.django-rest-framework.org
 - Django Rest API reference: https://www.bezkoder.com/django-rest-api/
 - Celery Documentation: https://docs.celeryq.dev/en/stable/index.html
 - Django Documentation: https://www.djangoproject.com