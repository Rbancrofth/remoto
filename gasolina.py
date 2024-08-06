
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('gasolina.csv')

# Configurar o estilo do gráfico
sns.set(style='whitegrid')

# Criar o gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='preço', data=df, marker='o')

# Adicionar título e rótulos aos eixos
plt.title('Preço da Gasolina entre os dias 01 e 10 de Julho')
plt.xlabel('Dia')
plt.ylabel('Preço em R$')

# Salvar o gráfico
plt.savefig('gasolina.png')

# Exibir o gráfico
plt.show()

# Comentário adicional para simular uma atualização
print("Gráfico gerado e salvo como gasolina.png")
