import requests
import json
import re
import pprint

api_key = "ApiKey cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw=="
url = "https://api-publica.datajud.cnj.jus.br/api_publica_tjrj/_search"
headers = {'Authorization': api_key,
           'Content-Type': 'application/json'}


payload = json.dumps({
  "size":5000,
  "query": {"match" : {"assuntos.codigo": 3431
                       }
            },
  "sort":[{"dataAjuizamento":{ "order" : "asc" }}]
})


contador = 0
response = requests.request("POST",url,headers=headers, data=payload)
dadosBrutos = response.json()

dados_dict = dadosBrutos['hits']['hits']
for i in dados_dict:
    sort = i['sort']
    orgao = i['_source']['orgaoJulgador']
    strData = i['_source']['dataAjuizamento']
    numeroProcesso = i['_source']['numeroProcesso']
    if orgao['codigo'] == 8046:
        vara = 'NOVA FRIBURGO 2 VARA CRIMINAL'
    elif orgao['codigo'] == 8047:
        vara = 'NOVA FRIBURGO 1 VARA CRIMINAL'
    assuntos = i['_source']['assuntos']
    formato = i['_source']['formato']['nome']
    ultimaAtualizacao = i['_source']['dataHoraUltimaAtualizacao']
    classe = i["_source"]['classe']['nome']
    padrao = re.compile(r'20[1-2]\d......')
    sort = i['sort'][0]
    if orgao['codigoMunicipioIBGE'] == 3303401 and padrao.match(strData):
        print(strData,classe, numeroProcesso, vara, formato, ultimaAtualizacao,sort)
        

