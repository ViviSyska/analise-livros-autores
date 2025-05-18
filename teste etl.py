import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo
caminho_arquivo = r'C:\Users\Nivia\Downloads\archive (3)\books.csv'

# Ler o arquivo CSV
df = pd.read_csv(caminho_arquivo, encoding='latin1')

# Calcular a contagem de livros por autor
contagem_autores = df['authors'].value_counts().reset_index()
contagem_autores.columns = ['author', 'number_of_books']

# Limitar aos 500 autores com mais livros
contagem_autores_50 = contagem_autores.head(50)

# Gráfico de barras
plt.figure(figsize=(18, 6))
plt.bar(contagem_autores_50['author'], contagem_autores_50['number_of_books'], color='steelblue')
plt.title('Contagem de Livros por Autor (Top 50)')
plt.xlabel('Autor')
plt.ylabel('Número de Livros')
plt.xticks(rotation=90, fontsize=7)
plt.tight_layout()
plt.show()
