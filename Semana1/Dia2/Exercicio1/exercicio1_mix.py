from transformers import pipeline
print("Vamos fazer um exercício de geração de texto, baseado em um tópico")

# NOTA: Se executar mais de uma vez ele tenta carregar novamente o modelo em memória!!!
# Inicializar pipeline de geração com modelo GPT-2
generator1 = pipeline('text-generation', model='pierreguillou/gpt2-small-portuguese')
# Inicializar pipeline de geração com modelo Gervasio
generator2 = pipeline('text-generation', model='PORTULAN/gervasio-7b-portuguese-ptpt-decoder')

# Pedir um tópico para o utilizador
prompt = input("Digite um tópico: ")

# Gerar Usando GPT-2 PT
resultado_gpt = generator1(prompt, max_length=100, truncation=False, num_return_sequences=1, temperature=0.5)
print("\n\nContinuação gerada (GPT-2 PT):", resultado_gpt[0]['generated_text'])

# Gerar Usando Gervasio PT
resultado_gervasio = generator2(prompt, max_length=100, truncation=False, num_return_sequences=1, temperature=0.5)
print("\n\nContinuação gerada (Gervasio PT):", resultado_gervasio[0]['generated_text'])