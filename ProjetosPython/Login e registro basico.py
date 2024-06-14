import os
import pandas as pd
import json


if os.path.isfile('sample.json') == True: 
  with open("sample.json","r") as reader:
    usuarios = json.load(reader)
else:
  usuarios = []
def registro():
    seu_login = input('Login: ')
    for i in usuarios:
      for k in i.values():
        if seu_login in (k.values()):
          print('Este login ja existe.')
          menu()
    sua_senha = input('Senha: ')
    id = len(usuarios) 
    if len(sua_senha) > 7:
      usuarios.append({id:{sua_senha:seu_login}})
    else:
      print('Sua senha é muito curta')
      menu()
    json_object = json.dumps(usuarios, indent = 4) 
    with open("sample.json", "w") as outfile:
      outfile.write(json_object)
    menu()
def entrada():
  eLogin = input('Digite aqui seu login: ')
  eSenha = input('Digite aqui sua senha: ')
  for i in usuarios:
    if {eSenha:eLogin} in i.values():
      print('Logado') ##
      menu()
    else:
      pass
  print("Nao Logado")
  menu()
def menu():
  opt = input('[1]Login\n[2]Register\n[3]Show\n[4]Close\n')
  if opt == '1':
    entrada()
  elif opt == '2':
    registro()
  elif opt == '3':
    for i in usuarios:
      print(i)
    menu()
  elif opt == '4':
    print('Até mais!!')
    exit()
  else:
    print('Digite uma opção válida.')
    menu()
menu()
