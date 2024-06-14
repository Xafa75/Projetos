import customtkinter as s
import datetime
data = datetime.date.today()
import pyodbc

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
    cliente VARCHAR(50) NOT NULL,
    servicos VARCHAR(100) NOT NULL,
    data_venda date NOT NULL,
    pago DECIMAL(6,2) NOT NULL,
    formaPagamento VARCHAR(8) NOT NULL,
    telefone DECIMAL(12) NOT NULL,
    primeiroCadastro BIT NOT NULL
    );"""
    cursor.execute(comando)
    cursor.commit()


def fechar(j):
    j.withdraw()
    janela.deiconify()


def enviar(nome,servicos,data, valor,formaPagamento,telefone, primeiroCadastro):
    comando = f"""INSERT INTO clientes(cliente, servicos, data_venda, pago, formaPagamento, telefone, primeiroCadastro)
    VALUES ('{nome}', '{servicos}','{data}', {valor}, '{formaPagamento}','{telefone}','{primeiroCadastro}')"""
        
    #Da o "Enter"
    cursor.execute(comando)

    #Confirma mudanças
    cursor.commit()
    janelaMenu = s.CTk() #Criando a janela

janelaMenu = s.CTk() #Criando a janela
janelaMenu.geometry("630x250") #Definindo o tamanho inicial da janela
janelaMenu.title("Cadastro de Serviços") #Definindo nome da janela
janelaMenu.resizable(False,False) #Trava a janela no tamanho definido
s.set_appearance_mode("Dark")  #Modo de aparencia do programa (Light ou Dark)
s.set_default_color_theme("dark-blue") #Modo de esquema de cores

LabelNome  = s.CTkLabel(janelaMenu, text="Nome:") #Label "Nome"
LabelNome.grid(row=1,column=1,pady=10, padx=15)

EntryNome = s.CTkEntry(janelaMenu, placeholder_text="Digite o nome", width=250) #caixa de entrada de nome
EntryNome.grid(row=1, column=2,pady=10,sticky="W")


LabelValor = s.CTkLabel(janelaMenu,text="Valor:") #Label "Valor"
LabelValor.grid(row=1,column=3, padx=10)

EntryValor = s.CTkEntry(janelaMenu, placeholder_text="Valor...", width=100) #Caixa de entrada do valor
EntryValor.grid(row=1, column=4,pady=10,sticky="W")

LabelNumero = s.CTkLabel(janelaMenu, text="Celular:") #Label "Celular"
LabelNumero.grid(row=2,column=1)

EntryNumero = s.CTkEntry(janelaMenu, placeholder_text="(99)99999-9999") #Caixa de entrada de numeros
EntryNumero.grid(row=2, column=2, sticky="W", padx=5,pady=10)

OPTPagamento = s.CTkOptionMenu(janelaMenu, values=["Outro","Cartão","Dinheiro","Pix"],width= 85)  #Menu de opções de pagamento
OPTPagamento.grid(row=1,column=5, padx=10)

LabelOBS = s.CTkLabel(janelaMenu, text="Serviços:") #Label "Serviços"
LabelOBS.grid(row=3, column=1)

EntryOBS = s.CTkTextbox(janelaMenu,height=100,width=300) #Caixa de entrada para serviços
EntryOBS.grid(row=3,column=2,columnspan=2,rowspan=3,pady=10)

ChkVisita = s.CTkCheckBox(janelaMenu,text="Primeiro Cadastro") #Check box primeiro cadastro
ChkVisita.grid(row=2, column=4)
    
BTNSalvar = s.CTkButton(janelaMenu,text="Salvar",width=100,command=lambda:enviar(EntryNome.get(),EntryOBS.get("1.0", "end-1c"),data,EntryValor.get(),OPTPagamento.get(),EntryNumero.get(), ChkVisita.get())) #Botão salvar
BTNSalvar.grid(row=6,column=5)



janelaMenu.mainloop()