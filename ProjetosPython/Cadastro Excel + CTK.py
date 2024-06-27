import customtkinter as s
import datetime
data = datetime.date.today()
data= data.strftime("%d/%m/%Y")
import pandas as pd
from tkinter import ttk
import openpyxl.workbook
import openpyxl
from openpyxl import Workbook,load_workbook
from os import path

diretorio = path.join(path.expanduser("~"), "Documents\\data.xlsx")
#Adicionar:

#fazer backup

#Automatizar procurações

global janelaPesquisa
global tree
def pesquisa(nomePesquisado):
    try:
        df = pd.read_excel(diretorio,sheet_name = 'Sheet') #guarda o arquivo excel em um dataframe
        df2 = df[df['nome'].str.contains(nomePesquisado)]
        janelaMenu.withdraw()
        JanelaPesquisa = s.CTkToplevel(janelaMenu)
        JanelaPesquisa.geometry("1000x600") #Definindo o tamanho inicial da janela
        JanelaPesquisa.title("Clientes Cadastrados") #Definindo nome da janela
        JanelaPesquisa.resizable(False,False)
        s.set_appearance_mode("Dark")
        df = pd.read_excel(diretorio,sheet_name = 'Sheet') #guarda o arquivo excel em um dataframe
        df2 = df[df['nome'].str.contains(nomePesquisado)]
        def dataframe_to_tk_treeview(root, dataframe):
            container = ttk.Frame(root)
            container.pack(fill='both', expand=True)

            # Criar o Treeview
            tree = ttk.Treeview(container)
            tree.pack(fill='both', expand=True)

            # Configurar colunas
            tree["columns"] = list(dataframe.columns)
            tree["show"] = "headings"

            # Adicionar cabeçalhos
            for column in dataframe.columns:
                tree.heading(column, text=column)

            # Adicionar dados
            for index, row in dataframe.iterrows():
                tree.insert("", "end", values=list(row))


            BTNVoltar = s.CTkButton(JanelaPesquisa,text="Voltar",command=lambda:Voltar(JanelaPesquisa))
            BTNVoltar.pack(padx=5, pady=5)
            return tree
        dataframe_to_tk_treeview(JanelaPesquisa,df2)
    except:
        statusvar.set("Ainda não há cadastros.").focus()

def Voltar(j):
    janelaMenu.deiconify()
    EntryNome.delete(0,"end")
    EntryNome.focus()
    j.withdraw()


def EnvioExcel(nome,servicos,dataVenda,pago,formaPagamento,telefone,primeiroCadastro): #Definindo a função
    statusvar.set("") #Limpa a variavel de status
    try: #Tenta acessar a tabela
        book = load_workbook(diretorio) #Define o book ultilizado
        sheet = book['Sheet'] #Define a pagina utilizada
        statusvar.set("Tabela encontrada") 
    except:
        clientes = ["nome", "servicos", "dataVenda", "pago", "formaPagamento", "telefone", "primeiroCadastro"]
        book = openpyxl.Workbook()
        sheet = book['Sheet']
        sheet.append(clientes) #Define o nome das colunas
        book.save(diretorio) 
        statusvar.set("Nova tabela criada")
        sheet.column_dimensions['A'].width = 25 #Seta o tamanho horizontal das colunas
        sheet.column_dimensions['B'].width = 30
        sheet.column_dimensions['C'].width = 11
        sheet.column_dimensions['F'].width = 12

    df = pd.read_excel(diretorio,sheet_name = 'Sheet') #guarda o arquivo excel em um dataframe
    if nome in df["nome"].values and dataVenda == data: #Checa se o nome ja foi cadastrado no dia
        statusvar.set("Cadastro repetido")

    elif nome == "" or pago == "":
        statusvar.set("Falta algo!")
        
    else:
        try:
            sheet.append([nome,servicos,dataVenda,pago,formaPagamento,telefone,primeiroCadastro]) #Guarda as opções passadas na função em uma linha do excel
            book.save(diretorio)
            statusvar.set("Cadastrado com sucesso!")
        except:
            statusvar.set("Feche o Excel!")
            
    EntryNome.delete(0,"end")
    EntryValor.delete(0,"end")
    EntryNumero.delete(0,"end")
    EntryOBS.delete('1.0',s.END)
    EntryNome.focus()
    

janelaMenu = s.CTk() #Criando a janela
janelaMenu.geometry("630x250") #Definindo o tamanho inicial da janela
janelaMenu.title("Cadastro de Serviços") #Definindo nome da janela
janelaMenu.resizable(False,False) #Trava a janela no tamanho definido
s.set_appearance_mode("Dark")  #Modo de aparencia do programa (Light ou Dark)
s.set_default_color_theme("dark-blue") #Modo de esquema de cores

statusvar = s.StringVar()
statusvar.set("Conectado!")
LabelCtrl = s.CTkLabel(janelaMenu, textvariable=statusvar, padx=10)
LabelCtrl.grid(row=6, column=2)

LabelNome  = s.CTkLabel(janelaMenu, text="Nome:") #Label "Nome"
LabelNome.grid(row=1,column=1,pady=10, padx=14)

EntryNome = s.CTkEntry(janelaMenu, placeholder_text="Digite o nome", border_color="Pink",width=250) #caixa de entrada de nome
EntryNome.grid(row=1, column=2,pady=10,sticky="W")

LabelValor = s.CTkLabel(janelaMenu,text="Valor:") #Label "Valor"
LabelValor.grid(row=1,column=3, padx=10)

EntryValor = s.CTkEntry(janelaMenu, placeholder_text="Valor...", border_color="Pink", width=100) #Caixa de entrada do valor
EntryValor.grid(row=1, column=4,pady=10,sticky="W")

LabelNumero = s.CTkLabel(janelaMenu, text="Celular:") #Label "Celular"
LabelNumero.grid(row=2,column=1)

EntryNumero = s.CTkEntry(janelaMenu, placeholder_text="(99)99999-9999",border_color="Pink") #Caixa de entrada de numeros
EntryNumero.grid(row=2, column=2, sticky="W", padx=5,pady=10)

OPTPagamento = s.CTkOptionMenu(janelaMenu, text_color="Black", fg_color="Pink",button_color="Pink", button_hover_color="Pink",values=["Outro","Cartão","Dinheiro","Pix"],width= 85)  #Menu de opções de pagamento
OPTPagamento.grid(row=1,column=5, padx=10)

LabelOBS = s.CTkLabel(janelaMenu, text="Serviços:") #Label "Serviços"
LabelOBS.grid(row=3, column=1)

LabelData = s.CTkLabel(janelaMenu,text=data) 
LabelData.grid(row=6,column=1,padx=10, sticky="S")

EntryOBS = s.CTkTextbox(janelaMenu,height=100,width=300,border_width=2,border_color="Pink") #Caixa de entrada para serviços
EntryOBS.grid(row=3,column=2,columnspan=2,rowspan=3,pady=10)

ChkVisita = s.CTkCheckBox(janelaMenu,text="Primeiro Cadastro",border_color="Pink",hover_color="Pink",fg_color="Pink",border_width=2) #Check box primeiro cadastro
ChkVisita.grid(row=2, column=4)
    
BTNSalvar = s.CTkButton(janelaMenu,text="Salvar", text_color="Black", fg_color="Pink",width=100,command=lambda:EnvioExcel(EntryNome.get(),EntryOBS.get("1.0", "end-1c"),data,EntryValor.get(),OPTPagamento.get(),EntryNumero.get(), ChkVisita.get())) #Botão salvar
BTNSalvar.grid(row=6,column=5)

BTNVer = s.CTkButton(janelaMenu,text="Pesquisar",text_color="Black", fg_color="Pink",command=lambda:pesquisa(EntryNome.get()),width=100) #Botao "Ver cadastros"
BTNVer.grid(row=6,column=4,padx=5)


janelaMenu.mainloop()