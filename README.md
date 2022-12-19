# DESAFIO TÉCNICO - ENGENHEIRO DE AUTOMAÇÃO E INTEGRAÇÃO

### O foco principal deste desafio é demonstrar a capacidade de implementar uma stack de integração de dados entre sistemas distribuídos com um mecanismo de mensageria para processamento em background. Será utilizada a stack Django (client) com Celery (task queue) e Redis (broker), e a integração dos dados será dada com a automação de requisições para os endpoints dos sistemas via tasks. Para fins de praticidade no deploy da stack, será utilizado docker-compose para montar toda a infraestrutura, que incluirá um banco de dados postgres e uma interface de monitoramento das tasks e workers do Celery com Flower.

## BUILD:

 - docker-compose build
 - docker compose up

### Abstraiu-se do desafio 3 sistemas distintos:
 - Website: Será representado como um app "website" no django com um endpoint para simular o POST do forms do lead.
 - Sistema de Automação de Marketing Digital: Será representado como um app "marketing" no django com um endpoint GET para inserção dos leads via task.
 - CRM: Será representado como um app "CRM" no django com varios endpoints para simular o fluxo de qualificação de leads, envio de forms e cadastro de clientes efetivos.

## FLUXO DOS DADOS:
 * 1 - Website lead forms POST
 * 1.1 - Digital marketing lead POST (automated with task)
 * 1.2 -CRM lead POST (automated with task)
 * 2 - CRM lead PUT qualified = true 
 * 2.1 - Send email to lead (automated with task)
 * 3 - Website costumer forms POST
 * 3.1 - CRM costumer POST (automated with task)

## SIMULANDO O FLUXO COM POSTMAN:
 * 1 - Usar postman para fazer as requisições externamente.

## OBSERVAÇÕES:
 * 1 - A task de envio de email ao qualificar o lead no CRM só funcionará se for especificado no arquivo .env as variáveis: EMAIL_ADDRESS e EMAIL_PASSWORD, credenciais obrigatoriamente de uma conta do gmail.
 * 2 - É possível também simular o fluxo pela interface web do django restframework, acessando as urls dos endpoints via o navegador.