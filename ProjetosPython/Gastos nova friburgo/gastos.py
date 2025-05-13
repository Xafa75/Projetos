import json
import pandas as pd
import matplotlib.pyplot as mpl

lista = []
valores = []
with open("entrada.json") as base:
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
    #print(ano,"|", mes,"|", unidade_gestora,"|", almoxarifado,"|", nota,"|", data_entrada,"|", tipo,"|", documento,"|", nome,"|", categoria,"|", valor,"\n")
    entrada = (ano, mes, unidade_gestora, almoxarifado, nota, data_entrada, tipo, documento, nome, categoria, valor)
    lista.append(entrada)
df = pd.DataFrame(lista, columns=("ano","mes","unidade_gestora", "almoxarifado","nota", "data_entrada", "tipo", "documento", "nome", "categoria", "valor"))
df.to_csv("gastosNF.csv")
print(df)