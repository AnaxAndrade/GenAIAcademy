# Dataset: Advertising
# Link do dataset: https://raw.githubusercontent.com/nguyen-toan/ISLR/master/dataset/Advertising.csv
import numpy as np
import pandas as pd

# 1. Carregar dataset Advertising
data = pd.read_csv("Advertising.csv")
# Remover possíveis colunas desnecessárias e preparar arrays numpy
X = data['TV'].values  # investimento em TV
y = data['Sales'].values  # vendas

# Opcional: normalizar X e y (aqui não necessário, pois já estão em escala comparável)

# 2. Inicializar parâmetros
beta0 = 0.0
beta1 = 0.0
alpha = 0.001
num_iters = 1000

n = len(X)  # número de exemplos

# Função auxiliar para calcular MSE (opcional, para monitorização)
def mean_squared_error(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()

# 3. Loop de Gradiente Descendente
for it in range(num_iters):
    # calcular previsões lineares
    y_pred = beta0 + beta1 * X
    # calcular gradientes
    grad0 = (2/n) * np.sum(y_pred - y)
    grad1 = (2/n) * np.sum((y_pred - y) * X)
    # atualizar parâmetros
    beta0 -= alpha * grad0
    beta1 -= alpha * grad1
    # opcional: imprimir erro a cada 100 iterações
    if it % 100 == 0:
        mse = mean_squared_error(y, y_pred)
        print(f"Iteração {it}: MSE = {mse:.4f}")

# 5. Após treino, mostrar parâmetros e um exemplo de previsão
# Em casos reais deveríamos armazenar os parâmetros beta0 e beta1 para utilização futura
print(f"Parâmetros obtidos: beta0 = {beta0:.3f}, beta1 = {beta1:.3f}")

print("O valor de investimento é em milhares de dólares, ex: 150 = $150 mil dólares")
investimento_ex = float(input("Introduza um valor de investimento: ")) #investidos em TV
pred_vendas = beta0 + beta1 * investimento_ex
print(f"Previsão de vendas para investimento TV = {investimento_ex}: {pred_vendas:.2f} (unidades em mil)")
