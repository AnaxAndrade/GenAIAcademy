# Vamos introduzir a componente de serviço do nosso RAG
O objetivo agora é que o nosso sistema de RAG sirva o conteúdo via Rest Web Service com a estrutura (request - response) indicada abaixo.
<br>
A sugestão é adicionar na script RAG o Flask

## Request
```
GET /rag

<DOMINIO:PORTA>/rag?q=<User question>

ex:

http://localhost:8080/rag?q=Qual+produto+a+empresa+X+tem+e+a+capgemini+não

```

## Response
```json
{
    "message": " A RESPOSTA DO LLM"
}
```