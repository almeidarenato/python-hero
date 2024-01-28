import random
# Personagem : classe mae
# Heroi : Controlado pelo usuario
# Inimigo: adversario do usuario

class Personagem:
    def __init__(self,nome,vida,nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Name: {self.get_nome()}\nHP: {self.get_vida()}\nLevel: {self.get_nivel()}"
    
    def atacar(self,alvo):
        dano = random.randint(self.__nivel*2,self.__nivel*4)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} used <<ATTACK ⚔️>> on {alvo.get_nome()} for {dano} of damage!!")
    
    def receber_ataque(self,dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel,habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
    
    def get_habilidade(self):
        return self.__habilidade

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nSkill: {self.get_habilidade()}"
    
    def ataque_especial(self,alvo):
        dano =  random.randint(self.get_nivel()*5,self.get_nivel()*8)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} used >>{self.get_habilidade()} ⚔️<< on {alvo.get_nome()} for {dano} of damage!!")
    
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel,tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nType: {self.get_tipo()}"


    

class Jogo:
    """ Classe orquestradora do jogo Python Hero """

    def __init__(self) -> None:
        self.heroi = Heroi(nome="Main Hero", vida=100, nivel=5, habilidade="Super Strenght")
        self.inimigo = Inimigo(nome="Bat",vida=50,nivel=3,tipo="Flying")
    
    def iniciar_batalha(self):
        print("Iniciando batalha")
        while self.heroi.get_vida() >0 and self.inimigo.get_vida()>0:
            print("\n Characters:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Press [ENTER] to attack...")
            escolha = input("Available Actions: \n[1] - Attack \n[2] - Skill) \n:")
            
            if(escolha == '1'):
                self.heroi.atacar(self.inimigo)
            elif(escolha == '2'):
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Choose a valid action")
            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)
            
        if self.heroi.get_vida() >0:
            print("Congrants, you won!")
        else:
            print("Game Over, Try again!")

# Criar instância do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()

