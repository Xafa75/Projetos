import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('Meu_Municipio_Acessos.csv',sep = ';') #Transforma o arquivo CSV em um DataFrame Pandas.

df_BandaLarga = df[df["Serviço"] == "Banda Larga Fixa"] # Separa apenas as linhas que contem o serviço de banda larga.
df_BandaLarga = df_BandaLarga[df_BandaLarga["Ano"] == 2024] # Separa apenas as linhas que contem o ano de 2024.

listaUF = list(set(df['UF'].tolist())) # Cria uma lista com todos os UF (Estados) presentes no dataframe, usando o método "set" para evitar itens repetidos.

ListaAcessos = df_BandaLarga.groupby("UF")['Acessos'].sum().to_list() # Agrupa os valores dos acessos por estado, somando seus valores e trasnformando em lista.

plt.bar(sorted(listaUF), ListaAcessos) # Cria um gráfico de barras, onde o eixo X são os valores da "ListaUF" e o eixo Y os valores de "ListaAcessos".
plt.ticklabel_format(style='plain', axis='y') # Evita que o Matplot use notação cientifica em valores muito grandes no eixo Y.

plt.xlabel('UF') # Legenda do eixo X
plt.ylabel('Aceesos de Banda larga') # Legenda do eixo Y
plt.title('Acesso de banda larga por estado') # Nome do gŕafico.

plt.show() # Mostra o gráfico.

