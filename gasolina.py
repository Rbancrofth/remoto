
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('gasolina.csv')

# Configurar o estilo do gráfico
sns.set(style='whitegrid')

# Criar o gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=df, marker='o')

# Adicionar título e rótulos aos eixos
plt.title('Preço da Gasolina ao Longo dos Dias')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')

# Salvar o gráfico
plt.savefig('gasolina.png')

# Exibir o gráfico
plt.show() 
