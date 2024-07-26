import requests
import json

api_key = "ApiKey cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw=="
url = "https://api-publica.datajud.cnj.jus.br/api_publica_tjrj/_search"
headers = {'Authorization': api_key,
           'Content-Type': 'application/json'}


payload = json.dumps({
  "size":300,
  "query": {
    "match": {"orgaoJulgador.codigoMunicipioIBGE":3303401},
    "match" : {"assuntos.codigo": 3431},

  }
})
contador = 0
response = requests.request("POST",url,headers=headers, data=payload)
dados_dict = response.json()
dados_dict = dados_dict['hits']['hits']
for i in dados_dict:
    orgao = i['_source']['orgaoJulgador']
    if orgao['codigoMunicipioIBGE'] == 3303401:
        print('friburgo',i['_source'].items())

