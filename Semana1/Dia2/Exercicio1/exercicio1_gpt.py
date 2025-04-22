from transformers import pipeline

# Inicializar pipeline de geração com modelo GPT-2 em português (ou inglês se preferido)
generator = pipeline('text-generation', model='pierreguillou/gpt2-small-portuguese')

# Prompt de exemplo (pode ser alterado pelos alunos)
prompt = "O gato é"

# Gerar texto continuando o prompt
resultados = generator(prompt, max_length=100, truncation=True, num_return_sequences=2, temperature=0.8)

print("Prompt:", prompt)
print("\n\nContinuação gerada[1]:", resultados[0]['generated_text'])
print("=======================================")
print("Continuação gerada[2]:", resultados[1]['generated_text'])