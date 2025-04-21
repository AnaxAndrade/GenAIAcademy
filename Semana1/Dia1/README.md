# Instalação base Python3 e Jupyter para AI/ML

## Verificar Python
Para verificar se o Python3 está instalado. Executar na linha de comandos:
```bash
python3 --version
```
Se não estiver instalado, obter do site oficial ou utilizar o gestor de pacotes do seu sistema operativo.
Existe alternativa de usar a ferramenta [Anaconda](https://anaconda.org/) para gestão da instalação do python, ambiente e dependências.

## Instalar Jupyter
```bash
# Atualizar o gestor de dependências (pip)
python3 -m pip install --upgrade pip
# Instalar jupyter - ferramena para programação interativa em python
python3 -m pip install jupyter
```

## Criar Ambiente Virtual
```bash
# Entrar na pasta do projeto
cd /pasta/do/projeto
# Criar o ambiente virtual para conter as dependências do projeto
python3 -m venv .venv
# Ativar o ambiente
source .venv/bin/activate
```
*(Em Windows: `.venv\Scripts\activate`)**

## Instalar Pacotes Principais
```bash
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow torch torchvision nltk spacy transformers
```

## Sobre as Bibliotecas Principais
- **NumPy**: permite computação numérica eficiente com matrizes e arrays.
- **Pandas**: manipulação e análise de grandes quantidades de dados tabulares.
- **Matplotlib** e **Seaborn**: visualização de dados com gráficos simples e avançados.
- **Scikit-learn**: algoritmos de machine learning para classificação, regressão, etc.
- **TensorFlow** e **Torch/Torchvision**: redes neuronais profundas e algoritmos de deep learning.
- **NLTK** e **spaCy**: processamento de linguagem natural.
- **Transformers**: modelos de linguagem avançados, incluindo BERT e GPT.

## Verificação do Ambiente
```python
import tensorflow as tf
import torch
print(f"TensorFlow: {tf.__version__}")
print(f"PyTorch: {torch.__version__}")
print(f"GPU Disponível: {torch.cuda.is_available()}")
```

## Executar Jupyter
```bash
jupyter lab
```


# Acesso ao Google Colab
O [Google Colab](https://colab.research.google.com/) é um ambiente gratuito de Jupyter Notebook que roda na nuvem e oferece acesso a GPUs e TPUs.


# Acesso a kaggle
O [Kaggle](https://www.kaggle.com/) é uma plataforma popular para competições de ciência de dados, datasets públicos e notebooks compartilhados pela comunidade.
