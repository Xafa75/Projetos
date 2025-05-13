rLogin = "Anthony"

rSenha = "senha01"

class CredencialErrada (Exception):
    def __init__(self,  nome, psw, mensagem = f"Algo deu errado, o login correto é {nome} e a senha é {psw}"):
        self.mensagem = mensagem
        self.nome = nome
        self.psw = psw
        super().__init__(self.mensagem)

def logar(rLogin, rSenha):
    login = input("Digite seu login")
    senha    = input("Digite sua senha")
    if login != rLogin and senha != rSenha:
        raise CredencialErrada(login, senha) 

logar()
