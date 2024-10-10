class char:
    def __init__(self, nome, vida, dano, armadura, hostilidade):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.armadura = armadura
        self.hostilidade = hostilidade
    
    def briga(self, alvo):
        if alvo.vida <= 0:
            print(alvo.nome + " Morto")
            exit()
        else:
            if self.dano <= alvo.armadura:
                alvo.armadura -= (self.armadura - int(10/100))
                print(f"{self.nome} não causou dano nenhum a {alvo.nome}, mas enfraqueceu sua armadura.")
            else:
                dano_real = self.dano - alvo.armadura
                alvo.vida -= dano_real
                print(f"Atacando {alvo.nome} em {dano_real} de dano." )
                if alvo.vida <= 0:
                    print(alvo.nome + " Morto")
                    exit()
                else:
                    print(f"Vida do {alvo.nome}: {alvo.vida}\n")
        if alvo.hostilidade == "Hostil":
            alvo.briga(self)
        else:
            self.briga(alvo)


personagem1 = char("Vector", 100, 30, 10, "Hosti")
personagem2 = char("Plinio", 100, 15, 20, "Hostil")

personagem1.briga(personagem2)
