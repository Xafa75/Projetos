import json
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:.2f}'.format

lista = []
valores = []
with open("ProjetosPython/Gastos nova friburgo/entrada.json") as base:
    dados = json.load(base)
for i in dados:
    ano = i["ano"]
    mes = i["mes"]
    unidade_gestora = i["unidade_gestora"]
    almoxarifado = i["almoxarifado"]
    nota = i["nota_fiscal"]
    data_entrada = i["data_entrada"]
    tipo = i["tipo"]
    documento = i["documento_favorecido"]
    nome = i["nome_favorecido"]
    categoria = i["categoria"]
    valor = i["valor"]
    valores.append(valor)
    entrada = (ano, mes, unidade_gestora, almoxarifado, nota, data_entrada, tipo, documento, nome, categoria, valor)
    lista.append(entrada)
df = pd.DataFrame(lista, columns=("ano","mes","unidade_gestora", "almoxarifado","nota", "data_entrada", "tipo", "documento", "nome", "categoria", "valor"))

df24 = df[df['ano'] == '2023']

dfMes = df24.groupby("mes")['valor'].sum().to_list()

listaMes= list(set(df['mes'].tolist()))
listaMesLimpa = []
for i in sorted(listaMes, key=lambda x: str(x)[:2]):
    if i == "03 - Marco":
        continue

    listaMesLimpa.append(i[5:])


print(df24)
print(dfMes)
print(listaMesLimpa)



plt.bar(listaMesLimpa,dfMes) # Cria um gráfico de barras, onde o eixo X são os valores da "ListaUF" e o eixo Y os valores de "ListaAcessos".
plt.ticklabel_format(style='plain', axis='y') # Evita que o Matplot use notação cientifica em valores muito grandes no eixo Y.

plt.xlabel('Mes') # Legenda do eixo X
plt.ylabel('Gasto') # Legenda do eixo Y
plt.title('Gasto da prefeitura por mês') # Nome do gŕafico.

plt.show() # Mostra o gráfico.

