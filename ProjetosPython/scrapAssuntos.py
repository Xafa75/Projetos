#O código a seguir é um Web Scraping que transforma a tabela de assuntos e seus respectivos códigos TPU (Tabelas Processuais Unificadas) em um DataFrame
#salvando-os em um arquivo csv, podendo ser usado posteriormente para qualquer fim educativo.

import requests
from bs4 import BeautifulSoup
import pandas as pd

def ScrapAssuntos():
    link = "https://www.tse.jus.br/servicos-judiciais/processos/processo-judicial-eletronico/tabela-de-assuntos-consolidada-todas-as-instancias-da-justica-eleitoral"
    response = requests.get(link)
    site = BeautifulSoup(response.content,"html.parser")
    td = site.findAll('td')
    lista = []
    for i in range(5,len(td),4):
        try:
            lista.append([str(td[i]).strip('</td>'),str(td[i+1]).strip('</td>')])
        except:
            pass
    df = pd.DataFrame(lista, columns=('Código','Assunto'))
    df.to_csv('tabela_assuntos.csv')
    print(df)
    return df

ScrapAssuntos()