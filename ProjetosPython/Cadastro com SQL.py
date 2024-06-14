import pyodbc
import datetime
import pandas as pd
import os

#Define a data atual
data = datetime.date.today()
data = data.strftime("%d-%m-%Y")

#Conecta no banco de dados na maquina local
print("Conectando ao banco de dados...")
dados_conexao = (
    "Driver={SQL SERVER};"
    "Server=Xafa-NTB;"
    "Database=cadastro_database;    "
)
#define a conexao a partir dos dados 
conexao = pyodbc.connect(dados_conexao)

#define o cursor (oque é escrito no prompt do SQL)
cursor = conexao.cursor()
print("Conexao bem sucedida\n")

#Checa se a tabela existe
try:
    comando = """SELECT * FROM clientes"""
    cursor.execute(comando)
    cursor.commit()

#Caso contrário cria uma tabela
except:
    print("Tabela nao encontrada, criando tabela...\n")
    comando = """CREATE TABLE clientes(
    serviço VARCHAR(50) NOT NULL,
    cliente VARCHAR(50) NOT NULL,
    data_venda date NOT NULL,
    pago DECIMAL(6,2) NOT NULL,
    pagamento VARCHAR(8) NOT NULL
    );"""
    cursor.execute(comando)
    cursor.commit()

#função do menu
def menu():
    print("Digite a seguir a opção desejada:\n ")
    print("[1] Adicionar novo cadastro")
    print("[2] Ver nomes cadastrados")
    print("[0] Sair")
    try:
        opc = int(input())
    except:
        print("Digite um  número!")
        menu()
    if opc == 1:
        print("Digite a seguir o nome a ser cadastrado:")

        #Define as variaveis a serem adicionadas no banco de dados.
        nome = input()
        preço = input("Valor gasto: ")
        print("[1] Pix \n[2] Dinheiro \n[3] Cartão\n")
        pagamento = input("Forma de pagamento:\n[1] Pix \n[2] Dinheiro \n[3] Cartão\n")
        if pagamento == 1:
            pagamento = "Pix"
        elif pagamento == 2:
            pagamento = "Dinheiro"
        elif pagamento == 3:
            pagamento = "Cartão"
        else:
            print("Opção inválida")
            os.system("cls")
            menu()
        #Cria o comando para inserir as informações previamente ditas.
        comando = f"""INSERT INTO clientes(serviço, cliente, data_venda, pago, pagamento)
        VALUES (1, '{nome}', '{data}', {preço}, '{pagamento}')"""
        
        
        #Da o "Enter"
        cursor.execute(comando)

        #Confirma mudanças
        cursor.commit()
        os.system("cls")
        menu()
    elif opc ==2:
        print("Nomes cadastrados:")

        #Seleciona todos da tabela clientes
        comando = """SELECT * FROM clientes
        ORDER BY data_venda"""
        cursor.execute(comando)

        #Pega todas as respostas
        resultado = cursor.fetchall()

        #Transforma em um dataframe do pandas
        df = pd.DataFrame(resultado)
        print(df, "\n")
        menu()
    elif opc == 0:
        print("Tchauu!!")
        os.system("cls")
        exit()
    else:
        print("Opção invalida.\n")
        os.system("cls")
        menu()

menu()