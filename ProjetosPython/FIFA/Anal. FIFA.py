import pandas as pd

#Importa o arquivo CSV para o programa e o transforma em DataFrame.
jogadores_fifa = pd.read_csv('male_players (legacy)_23.csv', sep=',', low_memory = False)

#Seleciona apenas as colunas das quais irá preciar.
df_limpo = jogadores_fifa[['short_name','wage_eur', 'fifa_version', 'overall', 'nationality_name']].sort_values(by='wage_eur')

#Organiza o DataFrame de acordo com o salário e pega apenas a primeira linha.
print(df_limpo.sort_values(by='wage_eur', ascending=False).head(1).to_string(index= False))

#Conta quantas vezes cada país aparece no DF. (Retira tambem o 'Name: count, dtype: int64')
maior_salario = df_limpo.sort_values(by='wage_eur', ascending=False).head(1)
print( f'O maior salário do FIFA é recebido por {maior_salario['short_name'].values[0]}, e é de {maior_salario['wage_eur'].values[0]} eur')


df_15 = df_limpo[df_limpo['fifa_version'] == 15]
df_16 = df_limpo[df_limpo['fifa_version'] == 16]
df_17 = df_limpo[df_limpo['fifa_version'] == 17]
df_18 = df_limpo[df_limpo['fifa_version'] == 18]
df_19 = df_limpo[df_limpo['fifa_version'] == 19]
df_20 = df_limpo[df_limpo['fifa_version'] == 20]
df_21 = df_limpo[df_limpo['fifa_version'] == 21]
df_22 = df_limpo[df_limpo['fifa_version'] == 22]
df_23 = df_limpo[df_limpo['fifa_version'] == 23]

lista_fifas = [df_15,df_16,df_17,df_18,df_19,df_20,df_21,df_21,df_22,df_23]

maior = 0
for i in range(len(lista_fifas)):
    if lista_fifas[i]['overall'].mean() > maior:
        maior = lista_fifas[i]['overall'].mean()
        versao_maior = lista_fifas[i]['fifa_version'].values
print(f'A maior média de pontuação overall é de {maior}, da versao do FIFA {versao_maior[0]}')


mais_jogadores = df_limpo['nationality_name'].value_counts().head(1)
print(f'O time com mais jogadores é {type(mais_jogadores)}')
'''
Quem recebe o maior salário do FIFA? V
Qual país tem mais jogadores? 
Qual ano teve o melhor overall? V
Qual a média de jogadores por FIFA?
'''