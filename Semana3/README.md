# Server de apoio e testes

## Modelos disponíveis
* LLM
    * llama3.3:70b
    * gemma3:27b
    * deepseek-r1:32b
* Exclusivo para embedding
    * nomic-embed-text

## Acessar Ollama server remoto
**Servidor:**  http://lab.entercoding.com:11434

**Passos:**

1. No código quando define o modelo, apontar para servidor do ollama com o endereço acima
2. Para exemplo, ver <u>test-serv.py</u> ou <u>test-serv.ipynb</u>


## Acessar Open Web UI Chat
**Servidor:**  http://lab.entercoding.com:3000 

**Passos:**

1. Abrir esse link no browser

2. Pode ser pedido email password para registar

3. Entrar, selecionar o modelo que quer "conversar", no canto superior esquerdo 


## Entrar na máquina
**Endereço servidor:** A ser fornecido on-demand, caso necessário

**Passos:**

1. Cada grupo vai ter uma chave ssh que pode usar para aceder diretamente ao servidor
2. Considerando que o servidor é linux ubuntu
3. O servidor é para ser acessado só em casos de precisar fazer fine tunning a um modelo ou teste pontual
4. Para acessar é preciso solicitar ao formador o IP atual da máquina
5. Para acessar para grupoX (ex: grupo8):
```bash
ssh -i /pasta/da/chave/grupo8_key grupo8@<IP-DA-MÁQUINA>
```