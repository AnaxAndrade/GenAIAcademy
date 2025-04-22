import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers

# 1. Carregar dataset de câncer de mama
data = load_breast_cancer()
X = data.data        # matriz de features (569 x 30)
y = data.target      # 0 = maligno, 1 = benigno

# Dividir entre treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


model = keras.Sequential([
    layers.Dense(16, activation='relu', input_shape=(X_train.shape[1],)),  # 30 -> 16 neurónios
    layers.Dense(1, activation='sigmoid')  # saída binária
])

# 3. Compilar modelo com otimizador e função de perda adequados
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 4. Treinar modelo por 20 épocas
history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2, verbose=0)

# 5. Avaliar no conjunto de teste
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Acurácia em teste: {accuracy*100:.2f}%")

# (Opcional) Exibir algumas previsões vs. verdadeiros
y_pred_prob = model.predict(X_test[:5])
y_pred = (y_pred_prob >= 0.5).astype(int).reshape(-1)
print("Previsto:", y_pred, "Real:", y_test[:5])
